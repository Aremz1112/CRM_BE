from django.contrib import admin
from django.urls import path, include
from .views import LoginUser, RegisterCustomer, UpdateCustomer, DeleteCustomer, FindACustomer, FindALLCustomer, UpdateUser, RegisterUser


urlpatterns = [
    path('FindACustomer/<str:id>', FindACustomer.as_view(), name="this api is used to find a customer") ,
    path('RegisterCustomer', RegisterCustomer.as_view(), name="this api is used to register a customer") ,
    path('UpdateCustomer/<str:id>', UpdateCustomer.as_view(), name="this api is used to update a customer record") ,
    path('DeleteCustomer/<str:id>', DeleteCustomer.as_view(), name="this api is used to delete a customer record") ,
    path('FindALLCustomer/<str:id>', FindALLCustomer.as_view(), name="this api is used to find all customer") ,
    path('RegisterUser', RegisterUser.as_view(), name="this api is used to register a user") ,
    path('login', LoginUser.as_view(), name="this api is used to login a user") ,
    path('UpdateUser',UpdateUser.as_view(), name="this api is used to Update a user") ,
    
    

]
