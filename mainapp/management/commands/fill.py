from django.core.management import BaseCommand
from mainapp.models import ProductCategory, Product,Contacts
from django.conf import settings
import json


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for cat in categories:
            # new_cat = ProductCategory(**cat)
            # new_cat.save()
            ProductCategory.objects.create(**cat)

        products = load_from_json('products')
        Product.objects.all().delete()
        for prod in products:
            category_name = prod['category']
            _cat = ProductCategory.objects.get(name=category_name)
            prod['category'] = _cat

            Product.objects.create(**prod)

        contacts = load_from_json('contact_locations')
        Contacts.objects.all().delete()
        for cont in contacts:
            Contacts.objects.create(**cont)
