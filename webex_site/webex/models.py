from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания", null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения", null=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация", null=True)
    discount = models.IntegerField(verbose_name='Скидка')
    left = models.IntegerField(verbose_name='Остаток')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование', null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

class Users(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    phone = models.IntegerField(verbose_name='Телефон')
    email = models.CharField(max_length=50, verbose_name='Почта')
    address = models.CharField(max_length=50, verbose_name='Адрес')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

class Order(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT, verbose_name='Номер пользователя')
    status = models.CharField(max_length=50, verbose_name='Статус заказа')
    payment_type = models.CharField(max_length=50, verbose_name='Тип оплаты')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


    class Meta:
        verbose_name = 'Статусы заказов'
        verbose_name_plural = 'Статусы заказов'
        ordering = ['id']

class order_product(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT, verbose_name='Номер заказа')
    production = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Номер товара')
    quantity = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Корзина заказов'
        verbose_name_plural = 'Корзина заказов'
        ordering = ['id']