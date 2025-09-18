from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Vehicle, ServiceRecord, Reminder
from .forms import VehicleForm, ServiceRecordForm, ReminderForm


# 👤 Signup view (for new user registration)
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tracker:vehicle-list')  # ✅ namespaced
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# 🔒 Mixin to ensure user can only access their own objects
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


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'tracker/vehicle_form.html'
    success_url = reverse_lazy('tracker:vehicle-list')  # ✅ fixed

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VehicleUpdateView(LoginRequiredMixin, UserOwnsObjectMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'tracker/vehicle_form.html'
    success_url = reverse_lazy('tracker:vehicle-list')  # ✅ fixed


class VehicleDeleteView(LoginRequiredMixin, UserOwnsObjectMixin, DeleteView):
    model = Vehicle
    template_name = 'tracker/vehicle_confirm_delete.html'
    success_url = reverse_lazy('tracker:vehicle-list')  # ✅ fixed


# 🧰 ServiceRecord Views
class ServiceRecordCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRecord
    form_class = ServiceRecordForm
    template_name = 'tracker/service_record_form.html'

    def dispatch(self, request, *args, **kwargs):
        # ensure the vehicle belongs to the logged-in user
        self.vehicle = get_object_or_404(Vehicle, pk=kwargs['vehicle_pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.vehicle = self.vehicle
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ✅ pass vehicle into template context so cancel button works
        context['vehicle'] = self.vehicle
        return context

    def get_success_url(self):
        return reverse('tracker:vehicle-detail', kwargs={'pk': self.vehicle.pk})  # ✅ fixed


class ServiceRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceRecord
    form_class = ServiceRecordForm
    template_name = 'tracker/service_record_form.html'

    def get_queryset(self):
        return ServiceRecord.objects.filter(vehicle__user=self.request.user)

    def get_success_url(self):
        return reverse('tracker:vehicle-detail', kwargs={'pk': self.object.vehicle.pk})  # ✅ fixed


class ServiceRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceRecord
    template_name = 'tracker/service_record_confirm_delete.html'

    def get_queryset(self):
        return ServiceRecord.objects.filter(vehicle__user=self.request.user)

    def get_success_url(self):
        return reverse('tracker:vehicle-detail', kwargs={'pk': self.object.vehicle.pk})  # ✅ fixed


# ⏰ Reminder Views
class ReminderCreateView(LoginRequiredMixin, CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'tracker/reminder_form.html'

    def dispatch(self, request, *args, **kwargs):
        # ensure the vehicle belongs to the logged-in user
        self.vehicle = get_object_or_404(Vehicle, pk=kwargs['vehicle_pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.vehicle = self.vehicle
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ✅ pass vehicle into template context so cancel button works
        context['vehicle'] = self.vehicle
        return context

    def get_success_url(self):
        return reverse('tracker:vehicle-detail', kwargs={'pk': self.vehicle.pk})  # ✅ fixed


class ReminderUpdateView(LoginRequiredMixin, UpdateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'tracker/reminder_form.html'

    def get_queryset(self):
        return Reminder.objects.filter(vehicle__user=self.request.user)

    def get_success_url(self):
        return reverse('tracker:vehicle-detail', kwargs={'pk': self.object.vehicle.pk})  # ✅ fixed


class ReminderDeleteView(LoginRequiredMixin, DeleteView):
    model = Reminder
    template_name = 'tracker/reminder_confirm_delete.html'

    def get_queryset(self):
        return Reminder.objects.filter(vehicle__user=self.request.user)

    def get_success_url(self):
        return reverse('tracker:vehicle-detail', kwargs={'pk': self.object.vehicle.pk})  # ✅ fixed
