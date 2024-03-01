
from django.contrib import admin
from django.urls import include, path
from MainApp import views

urlpatterns = [
    path('', views.home ),
    path('about', views.about),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/<int:item_id>/not_found/', views.item_not_found, name='item_not_found'),
    path('items/', views.all_items, name='all_items'),
]