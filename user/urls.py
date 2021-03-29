from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('last_h_Posts', views.last_h_Posts, name='last_h_Posts'),
    path('searchWord/', views.searchWord, name='searchWord')
]