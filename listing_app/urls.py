from listing_app import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('home', views.index, name='ld_home'),
    path('myorders', views.myorders, name='myorders'),
    path('return/rto', views.return_orders, name='return_orders'),
    #path('product', views.list_product, name='list_product'),
    path('cust_checkout', views.cust_checkout, name='cust_checkout'),

    path('icons', views.icons, name='ld_icons'),
    path('login', views.login, name='ld_login'),
    path('login_conf', views.login_conf, name='list_dash_login_conf'),
    path('register', views.register, name='ld_register'),
    path('lockscreen', views.lockscreen, name='ld_lockscreen'),

    path('product_elements', views.product_elements, name='ld_product_elements'),
    path('edit_product<int:id>', views.edit_product, name='ld_ed_product'),
    path('del_product<int:id>', views.del_product, name='ld_del_product'),
    path('product_table', views.product_table, name='ld_product_table'),

    path('logout', views.logout, name='list_dash_logout'),

    path('checkout_details_table', views.checkout_details_table, name='ld_checkout_details_table')

]