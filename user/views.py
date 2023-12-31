from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import UserForm, SigninForm
from news.forms import CommentForm
from .models import User
from news.models import News


def Home(request):
	news=News.objects.all()
	return render(request, 'home.html', {'newshome':news})


def Signup(request):
	form=UserForm()
	if request.method=='POST':
		form=UserForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'signup.html', {'form':form})
	return render(request, 'signup.html', {'form':form})


def Signin(request):
	Login=SigninForm()
	if request.method=='POST':
		Login=SigninForm(data=request.POST)
		if Login.is_valid():
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
		return render(request, 'signin.html', {'Login':Login})
	return render(request, 'signin.html', {'Login':Login})


def Logout(request):
	logout(request)
	return redirect('home')


def Profile(request):
	user=UserForm(instance=request.user)
	return render(request, 'profile.html', {'userprofile':user})

