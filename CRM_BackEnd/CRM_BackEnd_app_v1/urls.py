from .django contrib import admin
from django.urls import path, include
from .views import LoginUserAPIView, RegisterCustomerAPIView, UpdateCustomerAPIView, DeleteCustomer, FindACustomerAPIView, FindALLCustomerAPIView, RegisterUserAPIView


urlpatterns = [
    path('FindACustomer/<int:id>', FindACustomerAPIView.as_view(), name="this api is used to find a customer") ,
    path('RegisterCustomer/<int:id>', RegisterCustomerAPIView.as_view(), name="this api is used to register a customer") ,
    path('UpdateCustomer/<int:id>', UpdateCustomerrAPIView.as_view(), name="this api is used to update a customer record") ,
    path('DeleteCustomer/<int:id>', DeleteCustomerAPIView.as_view(), name="this api is used to delete a customer record") ,
    path('FindALLCustomer/<int:id>', FindALLCustomerAPIView.as_view(), name="this api is used to find all customer") ,
    path('RegisterUser/<int:id>', RegisterUserAPIView.as_view(), name="this app is used to register a user") ,
    
    

]
