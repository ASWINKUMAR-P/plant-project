from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginView, name='login'),
    path('home/', views.homepage, name='home'),
    path('showdata/', views.showdata, name='show'),
]