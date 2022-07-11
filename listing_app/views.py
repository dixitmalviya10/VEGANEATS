from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from dashapp.models import settings
from listing_app.forms import list_dash_product_form, list_dash_regist_form
from listing_app.models import list_dash_checkout_details, list_dash_product, list_dash_user_register

# Create your views here.

def index(request):
    if 'ld_n_name' in request.session:
        data = {
                'name' : request.session.get('ld_n_name')
            }
        ldfm = settings.objects.all()
        getprd = list_dash_product.objects.all()
        return render(request, 'listing_dash/index.html', {'d':data, 'sett_table':ldfm, 'getprd':getprd})
    return redirect('ld_login')

def myorders(request):
    if 'ld_n_name' in request.session:
        data = {
                'name' : request.session.get('ld_n_name')
            }
        ldfm = settings.objects.all()
        return render(request, 'listing_dash/myorders.html', {'d':data, 'sett_table':ldfm})
    return redirect('ld_login')

def return_orders(request):
    if 'ld_n_name' in request.session:
        data = {
                'name' : request.session.get('ld_n_name')
            }
        ldfm = settings.objects.all()
        return render(request, 'listing_dash/return.html', {'d':data, 'sett_table':ldfm})
    return redirect('ld_login')

# def list_product(request):
#     return render(request, 'listing_dash/listproduct.html')

def cust_checkout(request):
    if 'ld_n_name' in request.session:
        data = {
                'name' : request.session.get('ld_n_name')
            }
        ldfm = settings.objects.all()
        return render(request, 'listing_dash/custcheckout.html', {'d':data, 'sett_table':ldfm})
    return redirect('ld_login')



def icons(request):
    if 'ld_n_name' in request.session:
        data = {
                'name' : request.session.get('ld_n_name')
            }
        ldfm = settings.objects.all()
        return render(request, 'listing_dash/mdi.html', {'d':data, 'sett_table':ldfm})
    return redirect('ld_login')

def lockscreen(request):
    return render(request, 'listing_dash/lock-screen.html')

# def register(request):
#     return render(request, 'listing_dash/register-2.html')

# def login(request):
#     return render(request, 'listing_dash/login-2.html')


#<---------------------------------login, register, login_conf, logout--------------------------------->
def login(request):
    if 'ld_n_name' in request.session:
        return redirect('ld_home')
    return render(request, 'listing_dash/login-2.html')


def register(request):
    if request.method == 'POST':
        fm = list_dash_regist_form(request.POST)
        if fm.is_valid:
            fm.save()
            fm = list_dash_regist_form()
            return redirect('ld_login')
    fm = list_dash_regist_form()
    return render(request, 'listing_dash/register-2.html', {'reg':fm})



@csrf_exempt
def login_conf(request):
    uname = request.POST.get('u_name')
    password = request.POST.get('pass1')
    if 'ld_n_name' not in request.session:
        if request.method == 'POST':
            if list_dash_user_register.objects.filter(username=uname, password=password):
                obj = list_dash_user_register.objects.get(username=uname, password=password)
                request.session['ld_n_name']=obj.username
                #THE NEXT ONLY SHOWS USER NAME AND IMAGE ICON IN DASHBOARD
                return redirect('ld_home')
            else:
                return redirect('ld_login')
        else:
            return redirect('ld_login')
    else:
        return render(request, 'listing_dash/login-2.html')
    

def logout(request):
    del request.session['ld_n_name']
    return redirect('ld_login')
#<--------------------------------ENDS:- login, register, login_conf, logout--------------------------------->



#<---------------------------------------------------Product Functions -------------------------------------------------------------------->
def product_elements(request):
    if 'ld_n_name' in request.session:
        data = {
                'name' : request.session.get('ld_n_name')
            }
        ldfm = settings.objects.all()
        if request.method == 'POST':
            print('Hello World')
            fm = list_dash_product_form(request.POST or None, request.FILES or None)
            if fm.is_valid():
                fm.save()
                return redirect('ld_product_table')
        else:
            fm = list_dash_product_form()
            return render(request, 'listing_dash/product_elements.html', {'prod':fm, 'd':data, 'sett_table':ldfm})
    return redirect('ld_login')

def edit_product(request, id):
    if 'ld_n_name' in request.session:
        data = {
                'name' : request.session.get('ld_n_name')
            }
        ldfm = settings.objects.all()
        pi = list_dash_product.objects.get(id=id)
        if request.method == 'POST':
            fm = list_dash_product_form(request.POST or None, request.FILES or None, instance=pi)
            if fm.is_valid():
                fm.save()
                return redirect('ld_product_table')
        else:
            img_data = pi = list_dash_product.objects.filter(id=id).get()
            fm = list_dash_product_form(instance=pi)
            return render(request, 'listing_dash/edit_product.html', {'edit_prod':fm, 'id':id ,'i_mg':img_data, 'd':data, 'sett_table':ldfm})
    return redirect('ld_login')

def del_product(request, id):
    fm = list_dash_product.objects.get(id=id)
    fm.delete()
    return redirect('ld_product_table')


def product_table(request):
    if 'ld_n_name' in request.session:
        data = {
                'name' : request.session.get('ld_n_name')
            }
        ldfm = settings.objects.all()
        shw = list_dash_product.objects.all()
        return render(request, 'listing_dash/product.html', {'prod_table':shw, 'd':data, 'sett_table':ldfm})
    return redirect('ld_login')

#<---------------------------------------------------ENDS:- Product Functions ------------------------------------------------------------------>


def checkout_details_table(request):
    if 'ld_n_name' in request.session:
        data = {
                'name' : request.session.get('ld_n_name')
            }
        ldfm = settings.objects.all()
        fm = list_dash_checkout_details.objects.all()
        return render(request, 'listing_dash/check_table.html', {'ch_table':fm, 'd':data, 'sett_table':ldfm})
    return redirect('ld_login')