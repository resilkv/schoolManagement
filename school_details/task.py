from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.decorators import task
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from school2.settings import EMAIL_HOST_USER
from .models import CustomUser

@task
def send_mail_to(id,message):

    user=CustomUser.objects.get(id=id)
    recipient_list=user.email
    

    send_mail(id,'mark updated',EMAIL_HOST_USER,[user.email],fail_silently= False)


    return None 