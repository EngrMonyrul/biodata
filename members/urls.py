from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:pk>', views.deletepeople, name='delete-people'),
]
