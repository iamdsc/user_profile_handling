from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import FileForm
from .models import MyFile

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

def list_file(request):
	return render(request, 'main/files.html')

def file_upload(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			obj=MyFile(title=form.cleaned_data.get('title'),
					   description=form.cleaned_data.get('description'),
					   owner=request.user,
					   file=request.FILES['file'])
			obj.save()
			return redirect('/files')
	else:
		form=FileForm()
	return render(request, 'main/upload.html', {'form':form})


