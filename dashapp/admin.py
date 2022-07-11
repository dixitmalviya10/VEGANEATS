from django.contrib import admin

from dashapp.models import category, customer, home_slider, settings, social_icons, user_register

# Register your models here.

admin.site.register(user_register)
admin.site.register(category)
admin.site.register(customer)
admin.site.register(settings)
admin.site.register(home_slider)
admin.site.register(social_icons)