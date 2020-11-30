from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('insert/',views.insert_operation,name='insert_operation'),
    path('update/',views.update_operation,name='update_operation'),
    path('withdraw/',views.withdraw_operation,name='withdraw_operation'),
    
]
