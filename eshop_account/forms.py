from django import forms
from django.contrib.auth.models import User
from django.core import validators
from utilities.forms import FormWithCaptcha


class UserEditForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام', 'class': 'form-control'}),
        label='نام',
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی', 'class': 'form-control'}),
        label='نام خانوادگی',
    )


class LoginForm(FormWithCaptcha):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label='نام کاربری',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'پسورد'}),
        label='پسورد',
        validators=[
            validators.MaxLengthValidator(25, 'تعداد کاراکترهای پسورد نباید بیشتر از ۲۵ باشد.'),
            validators.MinLengthValidator(6, 'تعداد کاراکترهای پسورد نباید کمتر از ۶ باشد.')
        ]
    )


class RegisterForm(FormWithCaptcha):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label="نام کاربری"
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
        label="ایمیل",
        validators=[
            validators.MaxLengthValidator(42, 'تعداد کاراکترهای ایمیل نباید کمتر از ۴۲ باشد.')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'پسورد'}),
        label="پسورد",
        validators=[
            validators.MaxLengthValidator(25, 'تعداد کاراکترهای پسورد نباید بیشتر از ۲۵ باشد.'),
            validators.MinLengthValidator(6, 'تعداد کاراکترهای پسورد نباید کمتر از ۶ باشد.')
        ]
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار پسورد'}),
        label='تکرار پسورد',
        validators=[
            validators.MaxLengthValidator(25, 'تعداد کاراکترهای پسورد نباید بیشتر از ۲۵ باشد.'),
            validators.MinLengthValidator(6, 'تعداد کاراکترهای پسورد نباید کمتر از ۶ باشد.')
        ]
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_exists_user = User.objects.filter(username=username).exists()
        if is_exists_user:
            raise forms.ValidationError("این نام کاربر قبلا ثبت شده است.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_exists_email = User.objects.filter(email=email).exists()
        if is_exists_email:
            raise forms.ValidationError("این ایمیل قبلا ثبت شده است")
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("پسوردها مغایرت دارند.")
        return re_password

