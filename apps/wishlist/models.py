
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

class UserManager(models.Manager):
	def validate_user(request, postData):
		errors = {}

		#name validation
		if len(postData['name']) < 3:
			errors['name'] = "Name must be longer than 3 characters"

		#username validation
		if len(postData['username']) < 3:
			errors['username'] = "Username must be longer than 3 characters"

		#password validation
		if len(postData['password']) < 8:
			errors['password'] = "Password must be 8 characters in length"
			
		if postData['password'] != postData['cnfrm_password']:
			errors['cnfrm_password'] = "Passwords do not match"

		return errors

class WishManager(models.Manager):
	def validate_wish(request, postData):
		errors = {}

		if len(postData['w_name']) < 3 or postData['w_name'] == "":
			errors['wish_name'] = "Name must be longer than 3 characters/Name entry cannot be blank"

		return errors




class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password =  models.CharField(max_length=255)
	hire = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Wish(models.Model):
	w_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ManyToManyField(User)
	added_by = models.CharField(max_length=255, default="unknown")
	objects = WishManager()
