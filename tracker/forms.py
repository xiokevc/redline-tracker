from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vehicle, ServiceRecord, Reminder


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'vin', 'mileage']
        labels = {
            'make': 'Make',
            'model': 'Model',
            'year': 'Year',
            'vin': 'VIN',
            'mileage': 'Current Mileage',
        }
        widgets = {
            'year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
            'mileage': forms.NumberInput(attrs={'min': 0}),
        }


class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = ['date', 'service_type', 'notes', 'cost']
        labels = {
            'date': 'Service Date',
            'service_type': 'Service Type',
            'notes': 'Additional Notes',
            'cost': 'Cost ($)',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'cost': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['due_date', 'service_type', 'notes', 'cost', 'is_sent']
        labels = {
            'due_date': 'Due Date',
            'service_type': 'Service Type',
            'notes': 'Reminder Notes',
            'cost': 'Estimated Cost ($)',
            'is_sent': 'Email Sent?',
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'cost': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }

