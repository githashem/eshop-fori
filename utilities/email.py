from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings


class EmailService:

    @staticmethod
    def send_email(subject, to: list, template_name, context):
        html = render_to_string(template_name, context)
        message = strip_tags(html)
        send_mail(subject, message, settings.EMAIL_HOST_USER, to, html_message=html)
