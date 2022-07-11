from django import forms

from dashapp.models import category, customer, home_slider, settings, social_icons, user_register

class regist_form(forms.ModelForm):
    class Meta:
        model = user_register
        fields = '__all__'
        
        widgets = {
            
            'username' : forms.TextInput(attrs={'class':'form-control form-control-lg border-left-0','placeholder':"Username"}),
            'email' : forms.EmailInput(attrs={'class':'form-control form-control-lg border-left-0','placeholder':"Email"}),
            'password' : forms.PasswordInput(attrs={'class':'form-control form-control-lg border-left-0','placeholder':"Password"},render_value=True),
        }


class category_form(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'
        
        widgets = {
            
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':"Add New Category"})
        }




class customer_form(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        widgets = {
            'img' : forms.FileInput(attrs={'class':'form-control d-none', 'accept':'image/*', 'id':'file', 'onchange':'loadFile(event)'}),
            'desc' : forms.Textarea(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'position' : forms.TextInput(attrs={'class':'form-control'})
        }


class settings_form(forms.ModelForm):
    class Meta:
        model = settings 
        fields = '__all__'
        
        widgets = {
            
            'mobile_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'delivery_info' : forms.Textarea(attrs={'class':'form-control'}),
            'logo' : forms.FileInput(attrs={'class':'form-control d-none', 'accept':'image/*', 'id':'file', 'onchange':'loadFile(event)'}),
            'logo_tagline' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.Textarea(attrs={'class':'form-control'}),
            
        }

class social_icons_form(forms.ModelForm):
    class Meta:
        model = social_icons
        fields = '__all__'

        widgets = {
            'social_media' : forms.TextInput(attrs={'class':'form-control'}),
        }
        

class home_slider_form(forms.ModelForm):
    class Meta:
        model = home_slider
        fields = '__all__'
        widgets = {
            
            'slider_image' : forms.FileInput(attrs={'class':'form-control d-none', 'accept':'image/*', 'id':'file', 'onchange':'loadFile(event)'}),
            'slider_title' : forms.TextInput(attrs={'class':'form-control'}),
            'slider_description' : forms.Textarea(attrs={'class':'form-control'}),
            'slider_link' : forms.TextInput(attrs={'class':'form-control'}),
        }
    
    


        
        # widgets = {
        #     'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'states' : forms.Select(attrs={'class':'form-control'}),
        #     'street_address' : forms.TextInput(attrs={'class':'form-control'}),
        #     'city' : forms.TextInput(attrs={'class':'form-control'}),
        #     'postcode' : forms.NumberInput(attrs={'class':'form-control'}),
        #     'phone':forms.NumberInput(attrs={'class':'form-control'}),
        #     'email_address': forms.EmailInput(attrs={'class':'form-control'}),
        #     'user_id' : forms.HiddenInput(attrs={'name':'user_id'})
        # }