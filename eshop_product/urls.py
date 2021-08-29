from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/search/', views.SearchProductListView.as_view()),
    path('products/<pk>/', views.product_detail, name='product_detail'),
    path('products/category/<name_category>/', views.ProductListByCategory.as_view(), name="category"),
]

