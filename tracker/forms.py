from django import forms
from .models import Vehicle, ServiceRecord, Reminder

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'vin', 'mileage']

class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = ['date', 'service_type', 'notes', 'cost']

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['due_date', 'service_type', 'notes', 'cost', 'is_sent']
