from django.shortcuts import render, redirect
from .models import User, Message, Comment

# Create your views here.
def index(request):
	return render(request, 'Dashboard/index.html')

def sign_in(request):
		return render(request, 'Dashboard/sign_in.html')
			
def login(request):
	if User.userManager.sign_in(request.POST['email'], request.POST['password']) == True:
		name = User.objects.filter(email=request.POST['email'])
		print name
		for user in name:
			request.session['user_first']=user.first_name
			request.session['user_last']=user.last_name
			request.session['user_id']=user.id
			request.session['user_level']=user.user_level
		return redirect('/dashboard')
	else:
		return redirect('/sign_in')

def register(request):
	return render(request, 'Dashboard/register.html')

def dashboard(request):
	#if session admin or user
	users = User.objects.all()
	if not 'user_level' in request.session:
		return redirect("/")
	else:
		if request.session['user_level'] == 'admin':
			return render(request, 'Dashboard/admin_dash.html', context={'users':users})
		else:
			return render(request, 'Dashboard/dash.html', context={'users':users})
def show(request, id):
	#query for user id to go to profile
	users=User.objects.filter(id=id)
	messages=Message.objects.filter(message_owner=id)
	comments=Comment.objects.all()
	userobjects = User.objects.all()
	return render(request, 'Dashboard/show.html', context={'users':users, 'messages':messages, 'comments':comments, 'userobjects':userobjects})

def edit(request, id):
	users=User.objects.filter(id=id)
	return render(request, 'Dashboard/edit.html', context={'users':users})

def remove(request, id):
	User.userManager.remove(id)
	return redirect('/dashboard')	

def admin_edit(request, id):
	users = User.objects.filter(id=id)
	return render(request, 'Dashboard/admin_edit.html', context={'users':users})

def logoff(request):
	del request.session['user_level']
	del request.session['user_id']
	del request.session['user_first']
	del request.session['user_last']
	return redirect ('/')

def addnew(request):
	User.userManager.create(request.POST['email'], request.POST['first_name'], request.POST['last_name'], request.POST['password'])
	return render(request, 'Dashboard/new_user.html')

def create(request):
	# send us to user model and create object
	return redirect('/dashboard')

def update(request, id):
	User.userManager.update(id, request.POST['email'], request.POST['first_name'], request.POST['last_name'], request.POST['user_level'])
	return redirect('/dashboard')

def update_password(request, id):
	User.userManager.update_password(id, request.POST['password'])
	return redirect('/dashboard')

def edit_description(request, id):
	User.userManager.edit_description(id, request.POST['description'])
	return redirect('/dashboard')

def postm(request, id, uid):
	id=int(id)
	Message.messageManager.create(id, request.POST['message'], uid)
	return redirect('/show/' + uid)

def postc(request, uid, mid, id):
	# id=int(id)
	Comment.commentManager.create(uid, request.POST['comment'], mid)
	return redirect('/show/' + id)