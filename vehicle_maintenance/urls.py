from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Default Django auth views (login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),

    # Your app URLs
    path('', include(('tracker.urls', 'tracker'), namespace='tracker')),
]
