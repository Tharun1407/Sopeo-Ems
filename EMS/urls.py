
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('Create',views.Create ,name = "Create"),
    path('Employee',views.Employee,name = 'Employee'),
    path('EmployeeDetails/<int:id>/',views.EmployeeDetails,name="EmployeeDetails"),
    path('EditEmployee/<int:id>/',views.EditEmployee,name = "EditEmployee"),
    path('deleteEmployee/<int:id>/',views.deleteEmployee,name = "deleteEmployee"),
    path('update/<int:id>/',views.update,name="update"),
    path('onLeave',views.onLeave,name="onLeaveEmployee"),
    path('update_object/<int:id>/', views.update_object, name='update_view'),
    path('update_object1/<int:id>/', views.update_object1, name='update_view1')
]
