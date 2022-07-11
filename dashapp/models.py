from operator import truediv
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class user_register(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    

class category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class customer(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='products', blank=True, null=True)
    desc = RichTextField(blank=True, null=True)#RichTextField(blank=True,null=True)
    name = models.CharField(max_length=50) 
    position = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class settings(models.Model):
    id = models.AutoField(primary_key=True)
    mobile_no = models.IntegerField()
    email = models.EmailField(max_length=254)
    delivery_info = models.TextField()
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    logo_tagline = models.CharField(max_length=50)
    address = models.TextField()


class social_icons(models.Model):
    id = models.AutoField(primary_key=True)
    social_media = models.CharField(max_length=50)
    

class home_slider(models.Model):
    id = models.AutoField(primary_key=True)
    slider_image = models.ImageField(upload_to='slider_images', blank=True, null=True)
    slider_title = models.CharField(max_length=100, null=True)
    slider_description = RichTextField(blank=True,null=True)#RichTextField(blank=True,null=True)
    slider_link = models.CharField(max_length=100, null=True)
    