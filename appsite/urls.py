
#from django.contrib import admin
from django.urls import path, include
from .import views



urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('levels', views.levels, name="levels"),
    path('levels/<str:pk>/', views.level, name="level"),
    path('units/<str:pk>/', views.unit, name="unit"),

    path('levels/addlevel', views.addlevel, name="addlevel"),
    path('units/addunit', views.addunit, name="addunit"),
    path('units', views.units, name="units"),
    path('members', views.members, name="members"),


]
