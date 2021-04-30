from django.shortcuts import render, redirect
from django.contrib.auth.decorators import *
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from .models import *
# Create your views here.

@login_required
def inbox(request):
    user = request.user
    messages = Message.get_messages(user=user)
    print('message' + str(messages))
    active_direct = None
    directs = None

    if messages:
        print("message in")
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=user, recipient=message['user'])
        print(directs)
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
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
    print('to_user_username' + to_user_username)
    print(body)

    if request.method == "POST":
        to_user = User.objects.get(username=to_user_username)
        print(to_user)
        Message.send_messages(from_user=from_user, to_user=to_user, body=body)
        return redirect('messages:inbox')
    else:
        return HttpResponseBadRequest()
