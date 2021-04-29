from django.shortcuts import render
from django.contrib.auth.decorators import *

from .models import *
# Create your views here.

@login_required
def inbox(request):
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        print(message)
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
        