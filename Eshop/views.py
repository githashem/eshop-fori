from django.shortcuts import render
from django.http import HttpResponseNotFound
from eshop_sliders.models import Slider
from eshop_settings.models import Settings
from eshop_product.models import Product
import itertools
from utilities.email import EmailService


def footer(request):
    context = {
        'settings': Settings.object()
    }
    return render(request, 'shared/Footer.html', context=context)


def header(request):
    context = {}
    return render(request, 'shared/Header.html', context=context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    sliders = Slider.objects.all()

    most_visit_products = Product.objects.order_by('-visit_count').all()[:8]
    latest_products = Product.objects.order_by('-id').all()[:8]

    # EmailService.send_email('test subject',
    #                         ['PersonalHashem@gmail.com'],
    #                         'email/base.html',
    #                         {'title': 'test', 'description': 'test description'})

    context = {
        "sliders": sliders,
        'most_visit_products': my_grouper(4, most_visit_products),
        'latest_products': my_grouper(4, latest_products)
    }
    return render(request, 'home.html', context=context)


def about_page(request):
    context = {
        'settings': Settings.object()
    }
    return render(request, 'about.html', context=context)


def not_found(request, exception=None):
    return render(request, '404.html', {})
