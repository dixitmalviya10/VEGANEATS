from django.urls import path
from frontapp import views

urlpatterns = [
    path('', views.index),
    path('homepage', views.index, name='homepage'),
    path('shop', views.shop, name='shop_page'),
    
    path('wishlist', views.wishlist, name='wishlist_page'),
    path('single_product<int:id>', views.single_product, name='single_product_page'),
    
    path('cart', views.cart, name='cart_page'),
    path('checkout', views.checkout, name='checkout_page'),
    #path('delete_item_incart<int:id>', views.delete_item_incart, name='delete_item_incart'),
    
    # path('about', views.about, name='about_page'),
    # path('blog', views.blog, name='blog_page'),
    
    #path('contact', views.contact, name='contact_page'),
    
    path('website_regist', views.website_regist, name='website_regist'),
    path('website_login', views.website_login, name='website_login'),
    path('website_logout', views.website_logout, name='website_logout'),
    path('website_login_conf', views.website_login_conf, name='website_login_conf'),
    
    path('add_to_cart<int:id>', views.add_to_cart, name='add_to_cart'),
    
    #path('filter_shop', views.filter_shop, name='filter_shop')
    
    #path('checkout_conf', views.checkout_conf, name='checkout_conf'),
    path('your_orders', views.your_orders, name='your_orders'),
    #path('message_sent', views.message_sent, name='message_sent')
    
    #path('checkout_details_elements', views.checkout_details_elements, name='checkout_details_elements')
        
]