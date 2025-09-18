from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    # 🏠 Landing page (root URL)
    path('', views.landing, name='landing'),

    # 👤 Authentication URLs
    path('signup/', views.signup, name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    # 🚗 Vehicle URLs
    path('vehicles/', views.VehicleListView.as_view(), name='vehicle-list'),
    path('vehicles/add/', views.VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicles/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicles/<int:pk>/edit/', views.VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicles/<int:pk>/delete/', views.VehicleDeleteView.as_view(), name='vehicle-delete'),

    # 🧰 ServiceRecord URLs
    path('vehicles/<int:vehicle_pk>/service/add/', views.ServiceRecordCreateView.as_view(), name='service-record-create'),
    path('service/<int:pk>/edit/', views.ServiceRecordUpdateView.as_view(), name='service-record-update'),
    path('service/<int:pk>/delete/', views.ServiceRecordDeleteView.as_view(), name='service-record-delete'),

    # ⏰ Reminder URLs
    path('vehicles/<int:vehicle_pk>/reminder/add/', views.ReminderCreateView.as_view(), name='reminder-create'),
    path('reminder/<int:pk>/edit/', views.ReminderUpdateView.as_view(), name='reminder-update'),
    path('reminder/<int:pk>/delete/', views.ReminderDeleteView.as_view(), name='reminder-delete'),
]
