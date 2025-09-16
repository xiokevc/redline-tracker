from django.contrib import admin
from .models import Vehicle, ServiceRecord, Reminder

admin.site.register(Vehicle)
admin.site.register(ServiceRecord)
admin.site.register(Reminder)
