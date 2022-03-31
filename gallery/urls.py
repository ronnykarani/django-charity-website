from django.urls import path
from . import views


urlpatterns = [
    path('', views.photo_list, name='gallery'),
    path('<int:pk>/', views.detail_view, name='detail'),
]