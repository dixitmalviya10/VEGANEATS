from django.contrib import admin

from frontapp.models import c_cart, checkout, website_register,total

# Register your models here.

admin.site.register(website_register)
admin.site.register(c_cart)
admin.site.register(checkout)
admin.site.register(total)