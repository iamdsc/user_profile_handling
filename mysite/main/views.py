from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def homepage(request):
	return render(request=request,
				  template_name='main/home.html')

def register(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			# logging in the registered user
			login(request, user)
			return redirect('main:homepage')
	form = NewUserForm
	return render(request=request,
				  template_name='main/register.html',
				  context={'form':form})

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('main:homepage')
	form=AuthenticationForm()
	return render(request=request,
				  template_name='main/login.html',
				  context={'form':form})

def logout_request(request):
	logout(request)
	return redirect('main:homepage')
