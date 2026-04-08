from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, CustomerSerializer
from .models import User, Customer
from uuid import uuid4

# Create your views here.
class RegisterUser(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            data = UserSerializer(data=request.data)
            if data.is_valid():
                validated_data = data.validated_data
                user = User(userid=str(uuid4()),
                fullName=validated_data["fullName"],
                email=validated_data["email"],
                role=validated_data["role"])
                user.set_password(validated_data["password"])
                user.save()
                return Response({"success":"user registered successfully"}, status=201)
            else:
                return Response({"error":"forbidden"}, status=403)
        except Exception as e:
            return Response({"error":str(e)},status=400)

class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.filter(email=email)
        except User.DoesNotExist:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.check_password(password):
            return Response(
                {"detail": "Invalid password"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response({"success":"logged in successfully"}, status=200)
    

class RegisterCustomer(APIView):
    def post(self, request):
        try:
            data = CustomerSerializer(data=request.data)
            if data.is_valid():
                validated_data = data.validated_data
                customer=Customer(custid=validated_data["custid"],
                fullName=validated_data["fullName"],
                email=validated_data["email"],
                mobile=validated_data["mobile"],
                dob=validated_data["dob"],
                occupation=validated_data["occupation"],
                socialsURL=validated_data["socialsURL"],
                role=validated_data["role"])
                customer.save()
                return Response({"success":"customer registered successfully"}, status=201)
            else:
                return Response({"error":"forbidden"}, status=403)
        except Exception as e:
            return Response({"error":str(e)},status=400)

class UpdateCustomer(APIView):
    def put(self, request, id):
        try:
            customer = Customer.objects.get(custid=id)
            data = CustomerSerializer(data=request.data)
            if data.is_valid():
                validated_data = data.validated_data
                customer["custid"] = validated_data["custid"]
                customer["fullName"] = validated_data["fullName"]
                customer["email"] = validated_data["email"]
                customer["mobile"] = validated_data["mobile"]
                customer["dob"] = validated_data["dob"]
                customer["occupation"] = validated_data["occupation"]
                customer["socialsURL"] = validated_data["socialsURL"]
                customer["role"] = validated_data["role"]
                customer.save()
                serialized_customer = CustomerSerializer(customer)
                return Response(serialized_customer.data,status=200)
            else:
                return Response({"error":"invaild input"}, status=403)
        except Customer.DoesNotExist:
            return Response({"error":"Customer not found"}, status=400)

class DeleteCustomer(APIView):
    def delete(self, request, id):
        try:
            customer = Customer.objects.get(custid=id)
            customer.delete()
            return Response({"success":"user deleted successfully"}, status=200)
        except Customer.DoesNotExist:
            return Response({"error":"Bad request"}, status=400)
        
class FindACustomer(APIView):
    def get(self, request, id):
        try:
            customer = Customer.objects.get(custid=id)
            serialized_customer = CustomerSerializer(customer)
            return Response(serialized_customer.data, status=200)
        except Customer.DoesNotExist:
            return Response({"error":"Customer not found"},status=400)

class FindALLCustomer(APIView):
    def get(self, request,):
        try:
            customers = Customer.objects.all()
            serialized_customer = CustomerSerializer(customers, many=True)
            return Response(serialized_customer.data, status=200)
        except Customer.DoesNotExist:
            return Response({"error":"Customer not found"}, status=400)



