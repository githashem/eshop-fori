from django import forms
from captcha.fields import ReCaptchaField, ReCaptchaV3


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(
        label='ریکپتچا',
        widget=ReCaptchaV3(
            api_params={'hl': 'fa'}),
        error_messages={
            'required': 'لطفا ثابت کنید که ربات نیستید',
        }
    )
