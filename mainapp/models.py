from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# говорят хорошая библеотка,но не хочется сильно париться
# verbose_name  нужен для того, чтобы наши названия подтянулись в админку

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='Название')
    image = models.ImageField(upload_to='products/', blank=True)
    short_desc = models.CharField(max_length=255, blank=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена', default=0)
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Contacts(models.Model):
    city = models.CharField(max_length=100, verbose_name='Город')
    phone = models.CharField(max_length=14, unique=True, verbose_name='Телефон')
    email = models.CharField(max_length=128, unique=True, verbose_name='Почта')
    address = models.CharField(max_length=128, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'