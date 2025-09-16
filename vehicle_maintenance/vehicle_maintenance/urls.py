from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='vehicle-list', permanent=False)),
    path('', include('tracker.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout/password
]
