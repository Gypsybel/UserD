from __future__ import unicode_literals

from django.db import models

class userManager(models.Manager):
	def create(self, email, first_name, last_name, password):
		total = User.objects.all()
		if len(total) == 0:
			User.objects.create(email=email, first_name=first_name, last_name=last_name, password=password, user_level='admin')
		else:	
			User.objects.create(email=email, first_name=first_name, last_name=last_name, password=password, user_level='normal')

	def update(self, id, email, first_name, last_name, user_level):
		User.objects.filter(id=id).update(first_name=first_name)
		User.objects.filter(id=id).update(last_name=last_name)		
		User.objects.filter(id=id).update(email=email)
		User.objects.filter(id=id).update(user_level=user_level)

	def update_password(self, id, password):
		User.objects.filter(id=id).update(password=password)
	
	def remove(self, id):
		User.objects.filter(id=id).delete()	

	def sign_in(self, email, password):
		if User.objects.filter(email=email, password=password):
			return (True)
		else:
			return (False, 'login uncuccessfull')

	def edit_description(self, id, description):
		User.objects.filter(id=id).update(description=description)				

class messageManager(models.Manager):
	def create(self, id, message, uid):
		user = User.objects.get(id=id)
		Message.objects.create(message=message, message_user=user, message_owner=uid)

class commentManager(models.Manager):
	def create(self, uid, comment, mid):
		user = User.objects.get(id=uid)
		message = Message.objects.get(id=mid)
		Comment.objects.create(comment=comment, comment_user=user, comment_message=message)

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	user_level = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = userManager()
	objects = models.Manager()


class Message(models.Model):
	message = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	message_user = models.ForeignKey(User)
	message_owner = models.CharField(max_length=20)
	messageManager = messageManager()
	objects = models.Manager()

class Comment(models.Model):
	comment = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	comment_user = models.ForeignKey(User)
	comment_message = models.ForeignKey(Message)
	commentManager = commentManager()
	objects = models.Manager()