from django import forms
from listing_app.models import list_dash_checkout_details, list_dash_product, list_dash_user_register



class list_dash_regist_form(forms.ModelForm):
    class Meta:
        model = list_dash_user_register
        fields = '__all__'
        
        widgets = {
            
            'username' : forms.TextInput(attrs={'class':'form-control form-control-lg border-left-0','placeholder':"Username"}),
            'email' : forms.EmailInput(attrs={'class':'form-control form-control-lg border-left-0','placeholder':"Email"}),
            'password' : forms.PasswordInput(attrs={'class':'form-control form-control-lg border-left-0','placeholder':"Password"},render_value=True),
        }


class list_dash_product_form(forms.ModelForm):
    class Meta:
        model = list_dash_product
        fields = '__all__'
        widgets = {
            'img' : forms.FileInput(attrs={'class':'form-control d-none', 'accept':'image/*', 'id':'file', 'onchange':'loadFile(event)'}),
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':"Add Product Name"}),
            'price' : forms.NumberInput(attrs={'class':'form-control','placeholder':"Add Price"}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'list_name' : forms.HiddenInput(attrs={'value':'smith'}),
        }

class list_dash_checkout_details_form(forms.ModelForm):
    class Meta:
        model = list_dash_checkout_details
        fields = '__all__'