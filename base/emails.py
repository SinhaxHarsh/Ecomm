from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email):
    subject="Your Registeration Was Successful"
    email_from= settings.EMAIL_HOST_USER
    message = f'Your Account Has Been Registered With Us Successfully'
    send_mail(subject, message, email_from, [email])