from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    products_list = Product.objects.all()[:4]
    print(products_list.query)
    context = {
        'products': products_list
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    context = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)
