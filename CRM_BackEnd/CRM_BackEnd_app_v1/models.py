from django.db import models
from mongoengine import Document, ListField, StringField, EmailField
from datetime import datetime

# Create your models here.

class User(Document):
   full_name =StringField(max_length=200) 
   email = EmailField(max_length=200)
   password = StringField(max_length=200)
   roles = ListField(StringField())

class Customer(Document):
    custid= StringField(max_length=200)
    full_name= StringField(max_length=200)
    mobile= StringField(max_length=20)
    dob= DateField()
    date_created = datetime.now()
    occupation = StringField(max_length=20)
    socials_Url = StringField ()
    

