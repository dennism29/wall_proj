from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login_app.models import User
from .models import Message, Comment

def wall_display(request):
    context = {
        "all_messages": Message.objects.all(),
        "curr_user": User.objects.get(id=request.session['user_id']),
    }
    return render(request, "wall.html", context)

def post_message(request):
    if request.method == "POST":
        curr_user = User.objects.get(id=request.session['user_id'])
        new_message = Message.objects.create(message=request.POST['message'], user=curr_user)
        return redirect('/wall')

def logout(request):
    request.session.flush()
    return redirect('/')

def post_comment(request):
    if request.method == "POST":
        curr_user = User.objects.get(id=request.session['user_id'])
        curr_message = Message.objects.get(id=int(request.POST['message_id']))
        new_comment = Comment.objects.create(message=curr_message, user=curr_user, comment=request.POST['comment'])
        return redirect('/wall')

def delete_message(request, message_id):
    curr_message = Message.objects.get(id=message_id)
    curr_message.delete()
    return redirect('/wall')
# Create your views here.
