from django import forms
from .models import ShippingAdress

class ShippingAdressForm(forms.ModelForm):
    class Meta:
        model = ShippingAdress
        fields = [
            'user','country', 'state', 'city', 'line1', 'line2', 'reference', 'postal_code', 'cellphone', 'default'
        ]
        labels = {
            'default': 'Establecer como dirección principal',
        }
        widgets={
            'user':forms.HiddenInput,
            'country':forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Título'
                }),
            'state':forms.TextInput(attrs={
                    'class':'form-control',
                }),
            'city':forms.TextInput(attrs={
                    'class':'form-control'
                }),
            'line1':forms.TextInput(attrs={
                    'class':'form-control'
                }),
            'line2':forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Fecha de inicio'
                }),
            'reference':forms.TextInput(attrs={
                    'class':'form-control',
                }),
            'postal_code':forms.TextInput(attrs={
                    'class':'form-control',
                }),
            'cellphone':forms.TextInput(attrs={
                    'class':'form-control',
                }),
            'default':forms.CheckboxInput(attrs={
                    'class':'custom-checkbox',
                })
        }