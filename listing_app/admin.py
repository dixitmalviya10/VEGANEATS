from django.contrib import admin

from listing_app.models import list_dash_checkout_details, list_dash_product, list_dash_user_register

# Register your models here.

admin.site.register(list_dash_user_register)
admin.site.register(list_dash_product)
admin.site.register(list_dash_checkout_details)