from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.log, name='log'),
    path('user/<int:pk>/', views.controlUser)
]