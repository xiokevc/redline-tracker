from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Tracker app handles all auth and main pages
    path('', include('tracker.urls')),
]
