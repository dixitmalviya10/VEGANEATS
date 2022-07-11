from django.urls import path
from dashapp import views

urlpatterns = [
    path('', views.index,),
    path('home', views.index, name='home'),
    
    # path('buttons', views.buttons, name='buttons'),
    # path('typography', views.typography, name='typography'),
    
    # path('charts', views.charts, name='charts'),
    
    path('icons', views.icons, name='icons'),
    
    path('dash_login', views.login, name='dash_login'),
    path('logout', views.logout, name='logout'),

    path('login_conf', views.login_conf, name='login_conf'),
    path('register', views.register, name='register'),
    path('lockscreen', views.lockscreen, name='lockscreen'),


    path('form-elements', views.form_elements, name='form-elements'),
    path('ctg_table', views.ctg_table, name='ctg_table'),
    path('edit_category<int:id>', views.edit_category, name='edit_category'),
    path('delete<int:id>', views.delete_category, name='del_category'),



    path('customer_elements', views.customer_elements, name='customer_elements'),
    path('edit_customer<int:id>', views.edit_customer, name='ed_customer'),
    path('del_customer<int:id>', views.del_customer, name='del_customer'),
    path('customer_table', views.customer_table, name='customer_table'),
    
    
    path('settings_table', views.settings_table, name='settings_table'),
    # path('settings_elements', views.settings_elements, name='settings_elements'),
    path('edit_settings<int:id>', views.edit_settings, name='ed_settings'),
    path('del_settings<int:id>', views.del_settings, name='del_settings'),

    path('add_icons', views.add_icons, name='add_icons'),
    path('edit_icons<int:id>', views.edit_icons, name='edit_icons'),
    path('del_icons<int:id>', views.del_icons, name='del_icons'),
    
    path('slider_elements', views.slider_elements, name='slider_elements'),
    path('edit_slider<int:id>', views.edit_slider, name='ed_slider'),
    path('del_slider<int:id>', views.del_slider, name='del_slider'),
    path('slider_table', views.slider_table, name='slider_table'),
    
    #path('checkout_details_table', views.checkout_details_table, name='checkout_details_table')
    
]