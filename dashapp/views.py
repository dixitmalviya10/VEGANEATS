from django.shortcuts import redirect, render
from dashapp.forms import category_form, customer_form, home_slider_form, regist_form, settings_form, social_icons_form
from django.views.decorators.csrf import csrf_exempt
from dashapp.models import category, customer, home_slider, settings, social_icons, user_register

# Create your views here.

def index(request):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        
        getcatg = category.objects.all()
        fm = settings.objects.all()
        getcust = customer.objects.all()
        gethomesldr = home_slider.objects.all()
        return render(request, 'dash/index.html', {'d':data, 'gcatg':getcatg, 'gcust':getcust, 'ghomesldr':gethomesldr, 'sett_table':fm})
    return redirect('dash_login')


def icons(request):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        fm = settings.objects.all()
        return render(request, 'dash/mdi.html',{'d':data, 'sett_table':fm})
    return redirect('dash_login')


def lockscreen(request):
    return render(request, 'dash/lock-screen.html')


#<--------------------------------------------login, register, login_conf, logout---------------------------->
def login(request):
    if 'n_name' in request.session:
        return redirect('home')
    return render(request, 'dash/login-2.html')


def register(request):
    if request.method == 'POST':
        fm = regist_form(request.POST)
        if fm.is_valid:
            fm.save()
            fm = regist_form()
            return redirect('dash_login')
    fm = regist_form()
    return render(request, 'dash/register-2.html', {'reg':fm})

@csrf_exempt
def login_conf(request):
    uname = request.POST.get('u_name')
    password = request.POST.get('pass1')
    if 'n_name' not in request.session:
        if request.method == 'POST':
            if user_register.objects.filter(username=uname, password=password):
                obj = user_register.objects.get(username=uname, password=password)
                request.session['n_name']=obj.username
                #THE NEXT ONLY SHOWS USER NAME AND IMAGE ICON IN DASHBOARD
                return redirect('home')
            else:
                return redirect('dash_login')
        else:
            return redirect('dash_login')
    else:
        return render(request, 'dash/login-2.html')
    

def logout(request):
    del request.session['n_name']
    return redirect('dash_login')
#<---------------------------------------------------ENDS:- login, register, login_conf, logout---------------------------------------------->



#<---------------------------------------------------Catagory Functions ------------------------------------------------------------------>
def form_elements(request):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        if request.method == 'POST':
            fm = category_form(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('ctg_table')
        else:
            fm = category_form()   
            return render(request, 'dash/basic_elements.html', {'catg':fm, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')

def ctg_table(request):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        shw = category.objects.all()
        return render(request, 'dash/basic-table.html', {'catg_table':shw, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')


def edit_category(request, id):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        pi = category.objects.get(id=id)
        if request.method == 'POST':
            fm = category_form(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                return redirect('ctg_table')
        else:
            fm = category_form(instance=pi)
            return render(request, 'dash/edit.html', {'edit_catg':fm, 'id':id, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')


def delete_category(request, id):
    fm = category.objects.get(id=id)
    fm.delete()
    return redirect('ctg_table')
#<---------------------------------------------------ENDS:- Catagory Functions ------------------------------------------------------------------>


 
#<---------------------------------------------------Customer Functions -------------------------------------------------------------------->

def customer_elements(request):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        if request.method == 'POST':
            fm = customer_form(request.POST or None, request.FILES or None)
            if fm.is_valid():
                fm.save()
                return redirect('customer_table')
        else:
            fm = customer_form()
            return render(request, 'dash/customer_elements.html', {'cust':fm, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')

def edit_customer(request, id):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        pi = customer.objects.get(id=id)
        if request.method == 'POST':
            fm = customer_form(request.POST or None, request.FILES or None, instance=pi,)
            if fm.is_valid():
                fm.save()
                return redirect('customer_table')
        else:
            img_data = pi = customer.objects.filter(id=id).get()
            fm = customer_form(instance=pi)
            return render(request, 'dash/edit_customer.html', {'edit_cust':fm, 'id':id, 'i_mg':img_data, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')


def del_customer(request, id):
    fm = customer.objects.get(id=id)
    fm.delete()
    return redirect('customer_table')

def customer_table(request):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        fm = customer.objects.all()
        return render(request, 'dash/customer_table.html', {'cust_table':fm, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')

#<---------------------------------------------------ENDS:- Customer Functions -------------------------------------------------------------------->


#<---------------------------------------------------Settings Functions -------------------------------------------------------------------->

def edit_settings(request, id):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        pi = settings.objects.get(id=id)
        if request.method == 'POST':
            fm = settings_form(request.POST or None, request.FILES or None, instance=pi)
            if fm.is_valid():
                fm.save()
                return redirect('settings_table')
        else:
            logo_img =  settings.objects.filter(id=id).get()
            fm = settings_form(instance=pi)
            return render(request, 'dash/edit_settings.html', {'edit_sett':fm, 'id':id, 'logo_img':logo_img, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')
    
def del_settings(request, id):
    fm = settings.objects.get(id=id)
    fm.delete()
    return redirect('settings_table')

def settings_table(request):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        fm = settings.objects.all()
        return render(request, 'dash/settings_table.html', {'sett_table':fm, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')

def add_icons(request):
    if request.method=="POST":
        fm = social_icons_form(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect(settings_table)
    else:
        fm = social_icons_form()
        return render(request, 'dash/icons_elements.html', {'ai':fm})

def edit_icons(request):
    pi = social_icons.objects.get(id=id)
    if request.method=="POST":
        fm = social_icons_form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect(settings_table)
    else:
        fm = social_icons_form(instance=pi)
        return render(request, 'dash/edit_icon_elements.html')

def del_icons(request):
    dl = social_icons.objects.get(id=id)
    dl.delete()
    return redirect(settings_table)
#<---------------------------------------------------ENDS:- Settings Functions ------------------------------------------------------>



#<---------------------------------------------------Slider Functions -------------------------------------------------------------------->

def slider_elements(request):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        if request.method == 'POST':
            fm = home_slider_form(request.POST or None, request.FILES or None)
            if fm.is_valid():
                fm.save()
                return redirect('slider_table')
        else:
            fm = home_slider_form()   
            return render(request, 'dash/slider_elements.html', {'add_slider':fm, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')

def edit_slider(request, id):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        pi = home_slider.objects.get(id=id)
        if request.method == 'POST':
            fm = home_slider_form(request.POST or None, request.FILES or None, instance=pi,)
            if fm.is_valid():
                fm.save()
                return redirect('slider_table')
        else:
            img_data = home_slider.objects.filter(id=id).get()
            fm = home_slider_form(instance=pi)
            return render(request, 'dash/edit_slider.html', {'edit_slider':fm, 'id':id, 'i_mg':img_data, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')

def del_slider(request, id):
    fm = home_slider.objects.get(id=id)
    fm.delete()
    return redirect('slider_table')

def slider_table(request):
    if 'n_name' in request.session:
        data = {
                'name' : request.session.get('n_name')
            }
        stfm = settings.objects.all()
        fm = home_slider.objects.all()
        return render(request, 'dash/slider_table.html', {'slider_table':fm, 'd':data, 'sett_table':stfm})
    return redirect('dash_login')

#<---------------------------------------------------ENDS:- Slider Functions -------------------------------------------------------------------->

