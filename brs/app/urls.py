from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

app_name = 'app'

urlpatterns = [
    # path('', views.home, name="home" ),
    path('', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/add-review/', views.add_review, name='add_review'),


] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

