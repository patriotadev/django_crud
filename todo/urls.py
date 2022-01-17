from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete')
]
