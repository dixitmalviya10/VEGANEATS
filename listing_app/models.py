from tkinter.tix import Tree
from django.db import models
from ckeditor.fields import RichTextField
from dashapp.models import category
# Create your models here.


class list_dash_user_register(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username


class list_dash_product(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='products', blank=True, null=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = RichTextField(blank=True,null=True)#RichTextField(blank=True,null=True)
    #list_name = models.CharField(max_length=50,null=True)
    product_category = models.ForeignKey(category, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class list_dash_checkout_details(models.Model):
    
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    states = models.CharField(max_length=50, default='gujarat')
    street_address = models.TextField()
    city = models.CharField(max_length=50)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email_address = models.EmailField(max_length=254)