from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, CustomerSerializer
from .models import User, Customer
from uuid import uuid4
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

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

class UpdateUser(APIView):
    permission_classes = [AllowAny]
    def put(self, request, email):
        try:
            user = User.objects.get(email=email)

            serializer = UserSerializer(user, data=request.data, partial=True)

            if serializer.is_valid():
                validated_data = serializer.validated_data
                if "fullName" in validated_data:
                    user.fullName = validated_data.get("fullName", user.fullName)
                if "role" in validated_data:
                    user.role = validated_data.get("role", user.role)
                if "email" in validated_data:
                    user.email = validated_data.get("email", user.email)
                if "password" in validated_data:
                    user.set_password(validated_data["password"])

                user.save()

                return Response(UserSerializer(user).data, status=200)

            return Response(serializer.errors, status=400)

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
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
        token = AccessToken()
        token["userid"] = str(user.userid)
        token["email"] = user.email
        token["role"] = user.role

        response = Response(
            {
                "message": "Login successful",
                "access": str(token)
            },
            status=status.HTTP_200_OK
        )

        response.set_cookie(
            key="access_token",
            value=str(token),
            httponly=False,   # True in production
            secure=False,     # True in production (HTTPS)
            samesite="Lax",
            max_age=420
        )

        return response
    

class RegisterCustomer(APIView):
    def post(self, request):
        try:
            data = CustomerSerializer(data=request.data)
            if data.is_valid():
                validated_data = data.validated_data
                customer=Customer(custid=str(uuid4()),
                fullName=validated_data["fullName"],
                email=validated_data["email"],
                mobile=validated_data["mobile"],
                dob=validated_data["dob"],
                date_created=datetime.now(),
                occupation=validated_data["occupation"],
                socialsURL=validated_data["socialsURL"])
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

            serializer = CustomerSerializer(
                customer, 
                data=request.data, 
                partial=True
            )

            if serializer.is_valid():
                if "fullName" in validated_data:
                    user.fullName = validated_data.get("fullName", user.fullName)
                if "email" in validated_data:
                    user.email = validated_data.get("email", user.email)
                if "mobile" in validated_data:
                    user.mobile = validated_data.get("mobile", user.mobile)
                if "occupation" in validated_data:
                    user.occupation = validated_data.get("occupation", user.occupation) 
                if "dob" in validated_data:
                    user.dob = validated_data.get("dob", user.dob)
                if "socialsURL" in validated_data:
                    user.socialsURL = validated_data.get("socialsURL", user.socialsURL)
                serializer.save()
                return Response(serializer.data, status=200)

            return Response(serializer.errors, status=400)

        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=404)

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



