from django import forms
from django.contrib.auth import get_user_model,login,authenticate

UserModel = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario',
    widget=forms.TextInput(attrs={
        'class':'form-control'
    }),
    max_length=20, required=True)

    first_name = forms.CharField(label='Nombre',
    widget=forms.TextInput(attrs={
        'class':'form-control'
    }),
    required=True)

    last_name = forms.CharField(label='Apellidos',
    widget=forms.TextInput(attrs={
        'class':'form-control'
    }),
    max_length=20, required=True)

    email = forms.EmailField(label='Correo electrónico',
    widget=forms.EmailInput(attrs={
        'class':'form-control'
    }),
    required=True)
    
    password = forms.CharField(label='Contraseña',
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'password'
    }),
    min_length=8, required=True)

    password_confirm = forms.CharField(label='Confirmar contraseña',
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'password'
    }),
    min_length=8, required=True)

    def save(self):
        clean_data = self.data     
        username = clean_data.get('username')
        email =  clean_data.get('email')
        password = clean_data.get('password')
        first_name = clean_data.get('first_name')
        last_name = clean_data.get('last_name')

        instance = UserModel(username=username,email=email,first_name=first_name,last_name=last_name)
        instance.set_password(password)
        instance.save()

        return instance


        
    def clean_username(self):
        clean_data = super().clean()
        username = clean_data.get('username')
        try:
            UserModel.objects.get(username=username)
            raise forms.ValidationError('Este nombre de usuario ya ha sido creado')
        except UserModel.DoesNotExist:
            pass
        

    def clean_password(self):
        clean_data = self.data
        #print(clean_data)
        password = clean_data.get('password')
    
        password_confirm = clean_data.get('password_confirm')
        print(password_confirm,password)
        if not password==password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden')

        

    def clean(self):
        clean_data = self.data
        username = clean_data.get('username')
        email =  clean_data.get('email')
        if username and email is None:
            raise forms.ValidationError('Debes introducir el nombre de usuario o correo electrónico')