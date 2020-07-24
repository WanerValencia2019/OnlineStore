from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView

from .forms import RegisterForm

#MODELO DE USUARIO PERSONALIZADO
UserModel = get_user_model()

# Create your views here.
class LoginView(View):
	template_name='users/login.html'

	def get(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			messages.success(request,f'Bienvenido de nuevo a ChoquiFood {request.user.first_name} {request.user.last_name}')
			return redirect('home')

		return render(request,self.template_name)

	def post(self,request,*args,**kwargs):
		username=request.POST['username'] 
		password=request.POST['password']
		USER = authenticate(request,username=username,password=password)

		if USER:
			print(login(request,USER))
			messages.success(request,f'Bienvenido a ChoquiFood  {USER.first_name} {USER.last_name}')
			return redirect('home')
		
		return render(request,self.template_name,{'erros':'Los credenciales son incorrectos'})

class RegisterView(View):
	model = UserModel
	form_class = RegisterForm
	success_url = reverse_lazy('login')
	template_name = 'users/register.html'
	context_object_name = 'form'

	def get(self,request,*args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')

		return render(request,self.template_name,{'form':self.form_class})

	def post(self,request,*args, **kwargs):
		form = self.form_class(request.POST)
	
		if (form.is_valid()):
			USER = form.save()
			login(request,USER)
			return redirect('home')
		#print(form.errors)
		return render(request,self.template_name,{'form':form})

def configuration(request):

	return render(request,'users/configuration.html')
