from django.shortcuts import render, get_object_or_404
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

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {'name': 'Все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)

        context = {
            'links_menu': links_menu,
            'products': products_list,
            'category': category_item
        }

        return render(request, 'mainapp/products_list.html', context)

    context = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)
