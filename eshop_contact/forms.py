from django import forms
from django.core import validators
from utilities.forms import FormWithCaptcha


class ContactForm(FormWithCaptcha):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "اسم کامل", "class": "form-control"}),
        label="اسم کامل",
        validators=[
            validators.MaxLengthValidator(150, "اسم کامل باید کمتر از ۱۵۰ کاراکتر باشد"),
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "ایمیل", "class": "form-control"}),
        label="ایمیل",
        validators=[
            validators.MaxLengthValidator(100, "ایمیل باید کمتر از ۱۰۰ کاراکتر باشد"),
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "موضوع", "class": "form-control"}),
        label="موضوع",
        validators=[
            validators.MaxLengthValidator(200, "موضوع باید کمتر از ۲۰۰ کاراکتر باشد"),
        ]
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "پیام", "class": "form-control", "rows": "8"}),
        label="پیام",
        validators=[
            validators.MaxLengthValidator(300, "پیام باید کمتر از ۳۰۰ کاراکتر باشد"),
        ]
    )
