from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView

from .models import Vehicle, ServiceRecord, Reminder
from .forms import VehicleForm, ServiceRecordForm, ReminderForm


# 🏠 Landing page
def landing(request):
    if request.user.is_authenticated:
        return redirect('tracker:vehicle-list')
    return render(request, 'tracker/landing.html')


# 👤 Signup view
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tracker:vehicle-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# 👤 Login/Logout views
class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('tracker:landing')
    http_method_names = ['get', 'post']


# 🔒 Mixin to ensure user owns the object
class UserOwnsObjectMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


# 🚗 Vehicle Views
class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'tracker/vehicle_list.html'
    context_object_name = 'vehicles'

    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user)


class VehicleDetailView(LoginRequiredMixin, UserOwnsObjectMixin, DetailView):
    model = Vehicle
    template_name = 'tracker/vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_records'] = self.object.service_records.all()
        context['reminders'] = self.object.reminders.all()
        return context


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'tracker/vehicle_form.html'
    success_url = reverse_lazy('tracker:vehicle-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VehicleUpdateView(LoginRequiredMixin, UserOwnsObjectMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'tracker/vehicle_form.html'
    success_url = reverse_lazy('tracker:vehicle-list')


class VehicleDeleteView(LoginRequiredMixin, UserOwnsObjectMixin, DeleteView):
    model = Vehicle
    template_name = 'tracker/vehicle_confirm_delete.html'
    success_url = reverse_lazy('tracker:vehicle-list')


# 🧰 ServiceRecord Views
class ServiceRecordCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRecord
    form_class = ServiceRecordForm
    template_name = 'tracker/service_record_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.vehicle = get_object_or_404(Vehicle, pk=kwargs['vehicle_pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.vehicle = self.vehicle
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle'] = self.vehicle
        return context

    def get_success_url(self):
        return reverse('tracker:vehicle-detail', kwargs={'pk': self.vehicle.pk})


class ServiceRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceRecord
    form_class = ServiceRecordForm
    template_name = 'tracker/service_record_form.html'

    def get_queryset(self):
        return ServiceRecord.objects.filter(vehicle__user=self.request.user).select_related('vehicle')

    def get_success_url(self):
        # Ensure vehicle exists; fallback to vehicle list if missing
        vehicle_pk = self.object.vehicle.pk if self.object.vehicle else None
        return reverse('tracker:vehicle-detail', kwargs={'pk': vehicle_pk}) if vehicle_pk else reverse('tracker:vehicle-list')


class ServiceRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceRecord
    template_name = 'tracker/service_record_confirm_delete.html'

    def get_queryset(self):
        return ServiceRecord.objects.filter(vehicle__user=self.request.user).select_related('vehicle')

    def get_success_url(self):
        vehicle_pk = self.object.vehicle.pk if self.object.vehicle else None
        return reverse('tracker:vehicle-detail', kwargs={'pk': vehicle_pk}) if vehicle_pk else reverse('tracker:vehicle-list')


# ⏰ Reminder Views
class ReminderCreateView(LoginRequiredMixin, CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'tracker/reminder_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.vehicle = get_object_or_404(Vehicle, pk=kwargs['vehicle_pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.vehicle = self.vehicle
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle'] = self.vehicle
        return context

    def get_success_url(self):
        return reverse('tracker:vehicle-detail', kwargs={'pk': self.vehicle.pk})


class ReminderUpdateView(LoginRequiredMixin, UpdateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'tracker/reminder_form.html'

    def get_queryset(self):
        return Reminder.objects.filter(vehicle__user=self.request.user).select_related('vehicle')

    def get_success_url(self):
        vehicle_pk = self.object.vehicle.pk if self.object.vehicle else None
        return reverse('tracker:vehicle-detail', kwargs={'pk': vehicle_pk}) if vehicle_pk else reverse('tracker:vehicle-list')


class ReminderDeleteView(LoginRequiredMixin, DeleteView):
    model = Reminder
    template_name = 'tracker/reminder_confirm_delete.html'

    def get_queryset(self):
        return Reminder.objects.filter(vehicle__user=self.request.user).select_related('vehicle')

    def get_success_url(self):
        vehicle_pk = self.object.vehicle.pk if self.object.vehicle else None
        return reverse('tracker:vehicle-detail', kwargs={'pk': vehicle_pk}) if vehicle_pk else reverse('tracker:vehicle-list')
