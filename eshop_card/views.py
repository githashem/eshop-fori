from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from . import forms, models
from eshop_product.models import Product
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from django.conf import settings
import time


@login_required(login_url="/login")
def add_new_order(request):
    order_form = forms.OrderForm(request.POST or None)
    if order_form.is_valid():
        order = models.Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = models.Order.objects.create(owner_id=request.user.id)

        count = order_form.cleaned_data.get("count")
        if count <= 0:
            count = 1

        product_id = order_form.cleaned_data.get("product_id")
        product = Product.objects.get_by_id(product_id)
        order.orderdetail_set.create(product_id=product.id, count=count, price=product.price)
        return redirect(f"/products/{product.id}/")
    return redirect("/")


@login_required(login_url="/login")
def cart_page(request):
    context = {
        'order': None,
        'details': None
    }

    order = models.Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if order is not None:
        context['order'] = order
        context['details'] = order.orderdetail_set.all()

    return render(request, 'cart/cart_page.html', context=context)


@login_required(login_url='/login')
def remove_item_from_order(request, id_item=None):
    if id_item is None:
        raise Http404()
    else:
        try:
            order_detail = models.OrderDetail.objects.get(id=id_item, order__owner_id=request.user.id)
        except:
            raise Http404()
        order_detail.delete()
        return redirect("/cart/")


CallbackURL = 'http://localhost:8000/verify'  # Important: need to edit for realy server.
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')


@login_required(login_url='/login')
def pay_with_zarinpal(request):
    order = models.Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if order is not None:
        result = client.service.PaymentRequest(settings.MERCHANT_ZARINPAL, order.get_total(), 'description',
                                               f'{CallbackURL}/{order.id}/')
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))
    else:
        raise Http404


def verify(request, order_id=None):
    if order_id is None:
        raise Http404
    else:
        if request.GET.get('Status') == 'OK':
            try:
                order = models.Order.objects.get(id=order_id)
            except:
                raise Http404
            result = client.service.PaymentVerification(settings.MERCHANT_ZARINPAL, request.GET['Authority'], order.get_total())
            if result.Status == 100:
                order.is_paid = True
                order.payment_date = time.time()
                order.tracking_code = result.RefID
                order.save()
                return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
            elif result.Status == 101:
                return HttpResponse('Transaction submitted : ' + str(result.Status))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed or canceled by user')

