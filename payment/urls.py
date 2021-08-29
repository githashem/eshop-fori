from django.urls import path
from . import views

urlpatterns = [
    path('zarinpal/', views.pay_with_zarinpal, name='zarinpal'),
    path('verify/', views.verify, name='verify'),
]
