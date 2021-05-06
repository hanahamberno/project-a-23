from django.shortcuts import render, redirect
from django.contrib.auth.decorators import *
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

@login_required
def inbox(request):
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=user, recipient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
    print(messages)
    context = {
            'directs': directs,
            'messages': messages,
            'active_direct': active_direct,
    }
    return render(
        request=request,
        template_name='messages/inbox.html',
        context=context,
    )

@login_required
def directs(request, username):
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)

    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0
    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
    }

    return render(
        request=request,
        template_name='messages/inbox.html',
        context=context,
    )

@login_required
def sendDirect(request):
    # the person on the website
    from_user = request.user
    # the person who receives the messages
    to_user_username = request.POST.get('to_user')
    # the content of each message
    body = request.POST.get('body')

    if request.method == "POST":
        to_user = User.objects.get(username=to_user_username)
        Message.send_messages(from_user=from_user, to_user=to_user, body=body)
        return redirect('messages:inbox')
    else:
        return HttpResponseBadRequest()

@login_required
def userSearch(request):
    query = request.GET.get("q")
    context = {}

    if query:
        #icontains means case insensative
        users = User.objects.filter(Q(username__icontains=query))

        #(Seungeon)
        # Pagination
        # First is the object(model) to be split, Second is how many objects is there in one page
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
        }

    return render(
        request=request,
        template_name="messages/search_user.html",
        context=context
    )

@login_required
def newConversation(request, username):
    from_user = request.user
    from_user_username = from_user.username
    body = f"{from_user_username} is interested in messaging you!"

    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('usersearch')
    if from_user != to_user:
        Message.send_messages(from_user=from_user, to_user=to_user, body=body)
    return redirect('messages:inbox')

def deleteConversation(request, username):
    from_user = request.user
    Message.delete_messages(from_user, username)
    print("delete_view in")
    return redirect('messages:inbox')
