from .models import Customer, User
from rest_framework_mongoengine import serializers

class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model=User
        fields='__all__'



class CustomerSerializer(serializers.DocumentSerializer):
    class Meta:
        model=Customer
        fields='__all__'