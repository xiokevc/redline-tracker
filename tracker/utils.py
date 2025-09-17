from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_reminder_email(reminder):
    subject = f"Upcoming Service Reminder for {reminder.vehicle.make} {reminder.vehicle.model}"
    context = {
        'reminder': reminder,
        'user': reminder.vehicle.user,
    }
    message = render_to_string('tracker/emails/reminder_email.txt', context)
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [reminder.vehicle.user.email],
        fail_silently=False,
    )
