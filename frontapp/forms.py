from django import forms

from frontapp.models import website_register

class website_register_form(forms.ModelForm):
    class Meta:
        model = website_register
        fields = '__all__'
        widgets = {
            
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'myusername'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':"name@example.com"}),
            'password' : forms.PasswordInput(attrs={'class':'form-control','placeholder':"Password"},render_value=True),
            'user_image' : forms.FileInput(attrs={'class':'form-control d-none', 'accept':'image/*', 'id':'file', 'onchange':'loadFile(event)'}),
        }
        
        
# class c_cart_form(forms.ModelForm):
#     class Meta:
#         model = c_cart
#         fields = '__all__'
#         widgets={
#             'user_id' : forms.NumberInput(attrs={'class':'form-control'}),
#             'product_id' : forms.NumberInput(attrs={'class':'form-control'})
#         }