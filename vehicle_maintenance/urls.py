from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Tracker app (includes landing, auth, vehicles)
    path('', include(('tracker.urls', 'tracker'), namespace='tracker')),
]
