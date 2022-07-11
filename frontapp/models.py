from django.db import models

# Create your models here.
class website_register(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    user_image = models.FileField(upload_to='user_profile_images', blank=True, null=True)
    def __str__(self):
        return self.username
    

class c_cart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    total = models.IntegerField(null=True)


class total(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    product_name = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    total = models.IntegerField(null=True)


class checkout(models.Model):
    id = models.AutoField(primary_key=True)
    user_checkout_id = models.IntegerField()
    product_checkout_id = models.IntegerField()
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()
