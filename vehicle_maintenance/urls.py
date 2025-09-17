from django.contrib import admin
from django.urls import path, include
from tracker import views as tracker_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication URLs (login, logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # Custom signup view
    path('accounts/signup/', tracker_views.signup, name='signup'),

    # Include tracker app URLs with namespace
    path('', include(('tracker.urls', 'tracker'), namespace='tracker')),
]
