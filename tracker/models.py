from django.db import models
from django.contrib.auth.models import User

# 🚗 Vehicle model
class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=17, unique=True)
    mileage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    class Meta:
        ordering = ['make', 'model', '-year']
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"


# 🧰 Service Record model
class ServiceRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='service_records'
    )
    date = models.DateField()
    service_type = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.service_type} on {self.date} for {self.vehicle}"

    class Meta:
        ordering = ['-date']
        verbose_name = "Service Record"
        verbose_name_plural = "Service Records"


# ⏰ Reminder model
class Reminder(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='reminders'
    )
    due_date = models.DateField()
    service_type = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder: {self.service_type} due on {self.due_date} for {self.vehicle}"

    class Meta:
        ordering = ['due_date']
        verbose_name = "Reminder"
        verbose_name_plural = "Reminders"
