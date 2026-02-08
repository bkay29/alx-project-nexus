from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    send_mail(
        subject="Welcome to Our Store",
        message="Your account has been created successfully.",
        from_email="noreply@estore.com",
        recipient_list=[email],
        fail_silently=False,
    )