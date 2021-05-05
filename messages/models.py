from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max

from users.models import *
from social_app.models import *

# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='from_user',
    )

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='to_user',
    )

    body = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
    )

    date = models.DateTimeField(
        auto_now_add=True,
    )

    is_read = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return 'user ' + self.user.username + " " + self.body

    def send_messages(from_user, to_user, body):
        sender_message = Message(
            user=from_user, #seungeon
            sender=from_user, #seungeon
            recipient=to_user,# kathy
            body=body,
            is_read=True,
        )

        sender_message.save()

        recipient_message = Message(
            user=to_user, #kathy
            sender=from_user, #seungeon
            recipient=from_user, #kathy
            body=body,
        )

        recipient_message.save()

        return sender_message

    def get_messages(user):
        users = list()
        #.values() returns the dictionary of specific argument
        messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
        for m in messages:
            users.append({
                'user': User.objects.get(pk=m['recipient']),
                'last': m['last'],
                'unread': Message.objects.filter(user=user, recipient__pk=m['recipient'], is_read=False).count()
            })
        return users

    def delete_messages(from_user, user_to_be_deleted):
        Message.objects.filter(
            user__username=from_user, 
            sender__username=from_user,
            recipient__username=user_to_be_deleted
        ).delete()

        Message.objects.filter(
            user__username=user_to_be_deleted, 
            sender__username=from_user,
            recipient__username=from_user
        ).delete()

        Message.objects.filter(
            user__username=from_user, 
            sender__username=user_to_be_deleted,
            recipient__username=user_to_be_deleted
        ).delete()

        Message.objects.filter(
            user__username=user_to_be_deleted, 
            sender__username=user_to_be_deleted,
            recipient__username=from_user
        ).delete()

        return None