# E_commerce_App/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'discount': forms.NumberInput(attrs={'step': '0.01'}),
        }

class MobileForm(forms.Form):
    phone = forms.CharField(max_length=15, label="Mobile Number")

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, label="Enter OTP")