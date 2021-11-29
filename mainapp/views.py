from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')

def contact(request):
    return render(request, 'mainapp/contact.html')


links_menu = [
    {'link_name': 'home', 'name': 'Дом'},
    {'link_name': 'modern', 'name': 'Модерн'},
    {'link_name': 'office', 'name': 'Офис'},
    {'link_name': 'classic', 'name': 'Классика'},
]


def products(request, name=None):
    context = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)

def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, 'mainapp/products.html', context)

def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, 'mainapp/products.html', context)

def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, 'mainapp/products.html', context)

def products_classic(request):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, 'mainapp/products.html', context)


