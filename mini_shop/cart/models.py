from django.db import models

from catalog.models import Product, User


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        related_name='customer',
        on_delete=models.CASCADE,
        verbose_name='Покупатель'
    )
    products = models.ManyToManyField(
        Product,
        verbose_name='Товары',
        blank=True,
        through='ProductsInOrder'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer} - {self.pub_date}'


class ProductsInOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name='Товар',
        related_name='count_in_order',
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество товаров в заказе'
    )
