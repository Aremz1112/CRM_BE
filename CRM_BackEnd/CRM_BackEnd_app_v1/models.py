from django.db import models
from mongoengine import Document, ListField, StringField, EmailField, DateField
from datetime import datetime
from django.contrib.auth.hashers import check_password, make_password

# Create your models here.

class User(Document):
   userid = StringField()
   fullName =StringField(max_length=200) 
   email = EmailField(max_length=200, unique= True)
   password = StringField(max_length=200)
   role = ListField(StringField())

   def set_password(self, password):
      self.password = make_password(password)

   def check_password(self, password):
      return check_password(password, self.password)

   @property
   def is_authenticated(self):
      return True

class Customer(Document):
    custid= StringField(max_length=200)
    fullName= StringField(max_length=200)
    email = EmailField(max_length=200)
    mobile= StringField(max_length=20)
    dob= DateField()
    date_created = datetime.now()
    occupation = StringField(max_length=20)
    socialsURL = StringField ()
   
    
