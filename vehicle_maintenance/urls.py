from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from tracker import views as tracker_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👤 Custom user auth (signup/login/logout)
    path('accounts/signup/', tracker_views.signup, name='signup'),
    path(
        'accounts/login/',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'accounts/logout/',
        LogoutView.as_view(next_page='login', http_method_names=['get', 'post']),
        name='logout'
    ),

    # Tracker app
    path('', include(('tracker.urls', 'tracker'), namespace='tracker')),
]
