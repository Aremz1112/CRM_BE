from django.db import models
from mongoengine import Document, ListField, StringField, EmailField, DateField
from datetime import datetime

# Create your models here.

class User(Document):
   fullName =StringField(max_length=200) 
   email = EmailField(max_length=200)
   password = StringField(max_length=200)
   roles = ListField(StringField())

class Customer(Document):
    custid= StringField(max_length=200)
    fullName= StringField(max_length=200)
    email = EmailField(max_length=200)
    mobile= StringField(max_length=20)
    dob= DateField()
    date_created = datetime.now()
    occupation = StringField(max_length=20)
    socialsURL = StringField ()
    role = ListField(StringField())
    