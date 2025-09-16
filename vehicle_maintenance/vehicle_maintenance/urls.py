from django.contrib import admin
from django.urls import path, include
from tracker import views as tracker_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout

    # Custom signup view
    path('accounts/signup/', tracker_views.signup, name='signup'),

    # Your app routes
    path('', include('tracker.urls')),
]
