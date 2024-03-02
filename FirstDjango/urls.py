
from django.contrib import admin
from django.urls import include, path
from MainApp import views

urlpatterns = [
    path('', views.home ),
    path('about', views.about),
    path('item/<int:item_id>/', views.item),
]