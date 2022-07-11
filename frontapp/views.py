from django.shortcuts import redirect, render
from frontapp.models import website_register, c_cart,total
from dashapp.models import category, customer, home_slider, settings
from frontapp.forms import website_register_form
from listing_app.forms import list_dash_checkout_details_form
from listing_app.models import list_dash_checkout_details, list_dash_product

# Create your views here.

def index(request):
    if 'w_name' in request.session:
        data = {
                'id' : request.session.get('w_id'),
                'name' : request.session.get('w_name'),
                'wimage' : request.session.get('w_image')
            }
        
        fm = settings.objects.all()
        cust = customer.objects.all()
        hs = home_slider.objects.all()

        prd = list_dash_product.objects.all()
        return render(request, 'front/index.html', {'cust':cust, 'prod':prd, 'sett_table':fm, 'home_slide':hs, 'w':data})
    return redirect('website_login')

def shop(request):
    if 'w_name' in request.session:
        data = {
                'name' : request.session.get('w_name'),
                'wimage' : request.session.get('w_image')
            }
        fm = settings.objects.all()
        shw = category.objects.all()

        prd = list_dash_product.objects.all()
        return render(request, 'front/shop.html', {'catg_table':shw, 'prod':prd, 'sett_table':fm, 'w':data})
    return redirect('website_login')

def wishlist(request):
    if 'w_name' in request.session:
        data = {
                'name' : request.session.get('w_name'),
                'wimage' : request.session.get('w_image')
            }
     
        fm = settings.objects.all()
        return render(request, 'front/wishlist.html', {'sett_table':fm, 'w':data})
    return redirect('website_login')
    
def single_product(request, id):
    if 'w_name' in request.session:
        data = {
                'name' : request.session.get('w_name'),
                'wimage' : request.session.get('w_image')
            }
        fm = settings.objects.all()
        prod = list_dash_product.objects.filter(id=id).get()
    
        return render(request, 'front/product-single.html', {'pd':prod, 'sett_table':fm, 'w':data})
    return redirect('website_login')



# def checkout(request):
#     if 'w_name' in request.session:
#         data = {
#                 'name' : request.session.get('w_name'),
#                 'wimage' : request.session.get('w_image')
#             }
#         if request.method == 'POST':
#             ck_out = checkout_details_form(request.POST)
#             if ck_out.is_valid():
#                 ck_out.save()
            
#         else:
#             ck_out = checkout_details_form()   
#             fm = settings.objects.all()
#             return render(request, 'front/checkout.html', {'sett_table':fm, 'w':data, 'add_ch_details':ck_out})
#     return redirect('website_login')




# def about(request):
#     if 'w_name' in request.session:
#         data = {
#                 'name' : request.session.get('w_name'),
#                 'wimage' : request.session.get('w_image')
#             }
#         fm = settings.objects.all()
#         cust = customer.objects.all()
#         return render(request, 'front/about.html', {'sett_table':fm, 'w':data, 'cust':cust})
#     return redirect('website_login')

# def blog(request):
#     if 'w_name' in request.session:
#         data = {
#                 'name' : request.session.get('w_name'),
#                 'wimage' : request.session.get('w_image')
#             }
#         fm = settings.objects.all()
#         return render(request, 'front/blog.html', {'sett_table':fm, 'w':data})
#     return redirect('website_login')

# def contact(request):
#     if 'w_name' in request.session:
#         data = {
#                 'name' : request.session.get('w_name'),
#                 'wimage' : request.session.get('w_image')
#             }
#         fm = settings.objects.all()
#         prd = list_dash_product.objects.all()
#         return render(request, 'front/contact.html', {'sett_table':fm, 'w':data})
#     return redirect('website_login')

#<---------------------------------------------------login, register, login_conf, logout---------------------------------------------->

def website_regist(request):
    if request.method == 'POST':
        fm = website_register_form(request.POST)
        if fm.is_valid:
            fm.save()
            fm = website_register_form()
            return redirect('website_login')
    fm = website_register_form()
    return render(request, 'front/website_register.html', {'web_reg':fm})



def website_login(request):
    if 'w_name' in request.session:
        return redirect('homepage')
    return render(request, 'front/website_login.html')



def website_logout(request):
    del request.session['w_name']
    # del request.session['w_image']
    return redirect('website_login')



def website_login_conf(request):
    u_name = request.POST.get('w_name')
    u_password = request.POST.get('w_password')
    if 'w_name' not in request.session:
        if request.method == 'POST':
            if website_register.objects.filter(username = u_name, password = u_password):
                obj = website_register.objects.get(username = u_name, password = u_password)
                request.session['w_id']=obj.id
                request.session['w_name']=obj.username
                
                #THE NEXT ONLY SHOWS USER NAME AND IMAGE ICON IN DASHBOARD
                return redirect('homepage')
            else:
                return redirect('website_login')
        else:
            return redirect('website_login')
    else:
        return render(request, 'front/website_login.html')

#<---------------------------------------------------ENDS:- login, register, login_conf, logout---------------------------------------------->

def add_to_cart(request, id):
    if 'w_id' in request.session:
        u_id = request.session.get('w_id')
        userd = c_cart.objects.filter(user_id=u_id)
        datad = c_cart.objects.filter(product_id=id)
        
        if datad and userd:
            return redirect('homepage')
        
        else:
            carts = c_cart(user_id=u_id,product_id=id) #isme u_id ki value store ho rahi he user_id mae aur same to same id ki value store ho rahi he product_id me
            carts.save()
            
            data = {
                'name' : request.session.get('w_name'),
                'wimage' : request.session.get('w_image')
            }
            fm = settings.objects.all()
            prod = list_dash_product.objects.filter(id=id).get()
            return render(request, 'front/product-single.html', {'pd':prod, 'sett_table':fm, 'w':data})
    else:
        return render(request, 'front/website_login.html')


def cart(request):
    if 'w_name' in request.session:
        data = {
                'name' : request.session.get('w_name'),
                'wimage' : request.session.get('w_image')
            }
        
        u_id = request.session.get('w_id')
        
        ct_data = c_cart.objects.filter(user_id=u_id).all()
        pro = list_dash_product.objects.all()
        fm = settings.objects.all()
        # itcart = c_cart.objects.filter(user_id=u_id).all()
        return render(request, 'front/cart.html', {'sett_table':fm, 'w':data,'ct_data':ct_data,'pro':pro})
    return redirect('website_login')


# def checkout(request):
#     if 'w_name' in request.session:
#         data = {
#                 'name' : request.session.get('w_name'),
#                 'wimage' : request.session.get('w_image'),
#                 'wid' : request.session.get('w_id')
#             }
#         ch_id = request.session.get('w_id')

#         if request.method == 'POST':
#             u_name = request.POST.get('f_name')
#             u_lname = request.POST.get('l_name')
#             u_state = request.POST.get('state_name')
#             u_address = request.POST.get('address_name')
#             u_city = request.POST.get('city_name')
#             u_postcode = request.POST.get('postcode_no')
#             u_phone = request.POST.get('phone_no')
#             u_email = request.POST.get('email_add')
#             ck = list_dash_checkout_details(user_id=ch_id, first_name=u_name, last_name=u_lname, states=u_state, street_address=u_address, city=u_city, postcode=u_postcode, phone=u_phone, email_address=u_email,)
#             ck.save()

#         else:
#             ck_out = list_dash_checkout_details_form()
#             fm = settings.objects.all()
#             xxx = list_dash_checkout_details.objects.filter(user_id=ch_id).all()
#             return render(request, 'front/checkout.html', {'sett_table':fm, 'w':data, 'add_ch_details':ck_out, 'addrs':xxx})
#     return redirect('website_login')

def checkout(request):
    if request.method == 'POST':
        c_total = request.POST.get('total')
        for x in request.POST.get('quantity'):
            c_id = request.POST.get('c_id')
            c_qty = request.POST.get('quantity')
            w_id =  request.session.get('w_id')
            if total.objects.filter(user_id=w_id):
                total.objects.filter(user_id=w_id).update(product_name=c_id,quantity=c_qty,total=c_total)
                data = {
                    'name' : request.session.get('w_name'),
                    'wimage' : request.session.get('w_image'),
                    'wid' : request.session.get('w_id')
                }
                toatl = total.objects.filter(user_id=w_id).get()
                ck_out = list_dash_checkout_details_form() 
                fm = settings.objects.all()
                xxx = list_dash_checkout_details.objects.filter(user_id=w_id).all()
                return render(request, 'front/checkout.html', {'sett_table':fm, 'w':data, 'add_ch_details':ck_out, 'addrs':xxx, 'tot':toatl})
            else:
                cart_total = total(user_id=w_id,product_name=c_id,quantity=c_qty,total=c_total)
                cart_total.save()
                data = {
                    'name' : request.session.get('w_name'),
                    'wimage' : request.session.get('w_image'),
                    'wid' : request.session.get('w_id')
                }
                ck_out = list_dash_checkout_details_form()
                toatl = total.objects.filter(user_id=w_id).get()
                fm = settings.objects.all()
                xxx = list_dash_checkout_details.objects.filter(user_id=w_id).all()
                return render(request, 'front/checkout.html', {'sett_table':fm, 'w':data, 'add_ch_details':ck_out, 'addrs':xxx, 'tot':toatl})
    else:
        pass
# def delete_item_incart(request, id):
#     fm = c_cart.objects.get(id=id)
#     fm.delete()
#     return redirect('cart_page')


# def checkout_conf(request, id):
#     if 'w_id' in request.session:
#         u_id = request.session.get('w_id')
#         check_d = checkout.objects.filter(user_checkout_id=u_id)
#         ch_data = checkout.objects.filter(product_checkout_id=id)
        
#         if ch_data and check_d:
#             return redirect('homepage')
        
#         else:
#             checks = checkout(user_checkout_id=u_id,product_checkout_id=id) #isme u_id ki value store ho rahi he user_id mae aur same to same id ki value store ho rahi he product_id me
#             checks.save()
             
#             data = {
#                 'name' : request.session.get('w_name'),
#                 'wimage' : request.session.get('w_image')
#             }
#             fm = settings.objects.all()
#             prod_check = product.objects.filter(id=id).get()
#             return render(request, 'front/product-single.html', {'prd_check':prod_check, 'sett_table':fm, 'w':data})
#     return redirect('website_login')

# def your_orders(request):
#     if 'w_name' in request.session:
#         data = {
#                 'name' : request.session.get('w_name'),
#                 'wimage' : request.session.get('w_image')
#             }
#         u_id = request.session.get('w_id')
#         chk_data = checkout.objects.filter(user_checkout_id=u_id).all()

#         pro = list_dash_product.objects.all()
#         fm = settings.objects.all()
#         return render(request, 'front/your_orders.html', {'sett_table':fm, 'w':data, 'ct_data':chk_data, 'pro':pro})
#     return redirect('website_login')


def your_orders(request):
    if 'w_name' in request.session:
        data = {
                'name' : request.session.get('w_name'),
                'wimage' : request.session.get('w_image')
            }
        fm = settings.objects.all()
        return render(request, 'front/your_orders.html', {'sett_table':fm, 'w':data})
    return redirect('website_login')


# def message_sent(request):
#     if request.method == 'POST':
