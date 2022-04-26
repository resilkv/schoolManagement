from django.core.mail import send_mail
from school2.settings import EMAIL_HOST_USER
def send_mail_to(user, message, receivers):
    user=CustomUser.objects.get(id=id)

    send_mail(
        user,'mark updated',EMAIL_HOST_USER,[user.email],
    fail_silently= False)

