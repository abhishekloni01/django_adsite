from django.db import models
from django.db import connections

# Create your models here.
class content:
    htag:str
    para:str
    img:str

class Electronics:
    img:str
    title:str
    desc:str
    offer:bool

class Demo:
    name:str
    lname:str
    img:str
    offer:bool

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(default=0)
    msg = models.TextField(max_length=300)
    
    