from django.urls import path
from . import views

urlpatterns = [
    # Vehicle URLs
    path('vehicles/', views.VehicleListView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicles/create/', views.VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicles/<int:pk>/update/', views.VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicles/<int:pk>/delete/', views.VehicleDeleteView.as_view(), name='vehicle-delete'),

    # ServiceRecord URLs (nested under vehicles)
    path('vehicles/<int:vehicle_pk>/service-records/create/', views.ServiceRecordCreateView.as_view(), name='service-record-create'),
    path('service-records/<int:pk>/update/', views.ServiceRecordUpdateView.as_view(), name='service-record-update'),
    path('service-records/<int:pk>/delete/', views.ServiceRecordDeleteView.as_view(), name='service-record-delete'),

    # Reminder URLs (nested under vehicles)
    path('vehicles/<int:vehicle_pk>/reminders/create/', views.ReminderCreateView.as_view(), name='reminder-create'),
    path('reminders/<int:pk>/update/', views.ReminderUpdateView.as_view(), name='reminder-update'),
    path('reminders/<int:pk>/delete/', views.ReminderDeleteView.as_view(), name='reminder-delete'),
]
