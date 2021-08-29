import itertools
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
from eshop_tag.models import Tag
from django.http import Http404
from eshop_category.models import Category
from eshop_card.forms import OrderForm


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    queryset = models.Product.objects.filter(active=True)
    paginate_by = 3

    # paginator
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     paginator = context['paginator']
    #     current_page_number = self.request.GET.get("page")
    #     current_page_number = int(current_page_number) if current_page_number else 1
    #     context['page_numbers'] = paginator.get_elided_page_range(current_page_number, on_each_side=1, on_ends=1)
    #     return context


class ProductListByCategory(ListView):
    template_name = 'product/product_list.html'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        name_category = self.kwargs['name_category']
        # category = Category.objects.filter(slug__iexact=name_category).first()
        # if category is None:
        #     raise Http404("دسته بندی موردنظر یافت نشد!")
        return models.Product.objects.get_products_by_category(name_category)


def products_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category/products-category.html', context=context)


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    queryset = models.Product.objects.filter(active=True)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, pk):
    product = models.Product.objects.get_by_id(product_id=pk)
    if product is None or not product.active:
        raise Http404("Not Found!!!!!!!!!")

    # print(product.tag_set.all())
    # for tag in product.tag_set.all():
    #     print(tag.title)
    # tag = Tag.objects.first()
    # print(tag.products.all())

    product.visit_count += 1
    product.save()

    galleries = models.ProductGallery.objects.filter(product_id=product.id)
    galleries_list = my_grouper(3, galleries)

    related_products = models.Product.objects.filter(categories__product=product).distinct()
    grouped_related_products = my_grouper(3, related_products)

    context = {
        'product': product,
        'galleries': galleries_list,
        "grouped_related_products": grouped_related_products,
        'order_form': OrderForm(request.POST or None, initial={"product_id": product.id})
    }
    return render(request, 'product/product_detail.html', context=context)


class SearchProductListView(ListView):
    template_name = 'product/product_list.html'
    paginate_by = 3

    def get_queryset(self):
        s = self.request.GET.get("s")
        if s is not None:
            return models.Product.objects.search(s)
        return models.Product.objects.filter(active=True)
