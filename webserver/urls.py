from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="Main"),
    path('webserver/', views.webserver),
    path('webserver/details/<slug:slug>', views.details),
    path('template/', views.template, name="template"),
    path('login/', views.login),
    path('about/', views.about),
    path('login/action_page/', views.action_page),
]
