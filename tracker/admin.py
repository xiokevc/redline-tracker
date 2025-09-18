from django.contrib import admin
from .models import Vehicle, ServiceRecord, Reminder


class ServiceRecordInline(admin.TabularInline):
    model = ServiceRecord
    extra = 0
    readonly_fields = ('date', 'service_type', 'cost')
    can_delete = False


class ReminderInline(admin.TabularInline):
    model = Reminder
    extra = 0
    readonly_fields = ('due_date', 'service_type', 'is_sent')
    can_delete = False


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'vin', 'mileage', 'user')
    search_fields = ('make', 'model', 'vin', 'user__username')
    list_filter = ('year', 'make')
    inlines = [ServiceRecordInline, ReminderInline]
    ordering = ('make', 'model', '-year')


@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'service_type', 'date', 'cost')
    search_fields = ('vehicle__make', 'vehicle__model', 'service_type')
    list_filter = ('date', 'service_type')
    ordering = ('-date',)


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'service_type', 'due_date', 'is_sent')
    search_fields = ('vehicle__make', 'vehicle__model', 'service_type')
    list_filter = ('due_date', 'is_sent')
    ordering = ('due_date',)
