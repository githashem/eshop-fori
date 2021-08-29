from django.urls import path
from . import views

urlpatterns = [
    path("add-new-order/", views.add_new_order),
    path("remove-item-from-order/<id_item>", views.remove_item_from_order),
    path("cart/", views.cart_page),
    path("zarinpal/", views.pay_with_zarinpal),
    path("verify/<order_id>/", views.verify),
]
