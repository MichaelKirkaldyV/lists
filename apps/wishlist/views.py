from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from .models import *
from django.contrib import messages


def homepage(request):
	return render(request, "wishlist/login.html")

def register(request):
	errors = User.objects.validate_user(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/')

	else:
		name = request.POST['name']
		username = request.POST['username']
		password = request.POST['password']
		hire = request.POST['hire']
		hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

		User.objects.create(name=name, username=username, password=hashed_pw, hire=hire)
		user = User.objects.get(username=username)
		request.session['id'] = user.id
		return redirect('/')

	

def login(request):
	username = request.POST['username']
	password = request.POST['password']

	user = User.objects.filter(username=username)

	if len(user) > 0:
		this_password = bcrypt.checkpw(password.encode(), user[0].password.encode())
		if this_password:
			request.session['id'] = user[0].id
			return redirect('/dashboard')

		else:
			messages.error(request, "Incorrect username/password combination.")
			return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')


def dashboard(request):

	context = {
		"my_list": Wish.objects.filter(user__id__contains=request.session['id']),
		"user": User.objects.get(id=request.session['id']),
		"wishes": Wish.objects.all()
	}
	return render(request, "wishlist/dashboard.html", context)

def wish(request):
	return render(request, "wishlist/create.html")

def create_wish(request):
	errors = Wish.objects.validate_wish(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/wish')

	else:
		w_name = request.POST['w_name']
		user = User.objects.get(id=request.session['id'])
		wish_ = Wish(w_name=request.POST['w_name'], added_by=user.username)
		wish_.save()
		wish_.user.add(user)

		return redirect('/dashboard')

def wish_item(request, id):

	context = {
		"wish": Wish.objects.get(id=id),
		"users": User.objects.filter(id=id)
	}

	return render(request, "wishlist/wishview.html", context)

def remove_wish(request, id):
	wish = Wish.objects.get(id=id)
	wish.delete()

	return redirect('/dashboard')

def add_wish_list(request, id):
	wish = Wish.objects.get(id=id)
	user_ = User.objects.get(id=request.session['id'])
	wish.user.add(user_)
	return redirect('/dashboard')

		
