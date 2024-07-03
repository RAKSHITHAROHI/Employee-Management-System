from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('index/',views.index),
    path('add/<int:a>/<int:b>',views.add),
    path('Employee_list/',views.Employee_list,name='Employee_list'),
    path('AddEmployee',views.AddEmployee,name='AddEmployee'),
    path('Delete/<int:pk>',views.DeleteEmployee,name='DeleteEmployee'),  
    path('Edit/<int:pk>',views.EditEmployee,name='editEmployee')   
]
