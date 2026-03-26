from django.contrib import admin
from django.urls import path, include
from .views import LoginUser, RegisterCustomer, UpdateCustomer, DeleteCustomer, FindACustomer, FindALLCustomer, RegisterUser


urlpatterns = [
    path('FindACustomer/<int:id>', FindACustomer.as_view(), name="this api is used to find a customer") ,
    path('RegisterCustomer/<int:id>', RegisterCustomer.as_view(), name="this api is used to register a customer") ,
    path('UpdateCustomer/<int:id>', UpdateCustomer.as_view(), name="this api is used to update a customer record") ,
    path('DeleteCustomer/<int:id>', DeleteCustomer.as_view(), name="this api is used to delete a customer record") ,
    path('FindALLCustomer/<int:id>', FindALLCustomer.as_view(), name="this api is used to find all customer") ,
    path('RegisterUser/<int:id>', RegisterUser.as_view(), name="this app is used to register a user") ,
    
    

]
