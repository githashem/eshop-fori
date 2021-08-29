from django.shortcuts import render
from . import models, forms
from eshop_settings.models import Settings


def contact_page(request):
    contact_form = forms.ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get("full_name")
        email = contact_form.cleaned_data.get("email")
        subject = contact_form.cleaned_data.get("subject")
        message = contact_form.cleaned_data.get("message")
        models.Contact.objects.create(full_name=full_name, email=email, subject=subject, message=message)
        contact_form = forms.ContactForm()

    context = {
        "contact_form": contact_form,
        'settings': Settings.object()
    }
    return render(request, 'contact/contact-page.html', context=context)
