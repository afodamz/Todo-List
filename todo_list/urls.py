from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<List_id>', views.delete, name="delete"),
    path('cross/<List_id>', views.cross, name="cross"),
    path('uncross/<List_id>', views.uncross, name="uncross"),
    path('edit/<List_id>', views.edit, name="edit"),
]
