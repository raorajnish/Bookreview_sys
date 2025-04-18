from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name="login" ),
    path('logout/', views.logout_view, name="logout" ),
    path('register/', views.register_view, name="register" ),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

