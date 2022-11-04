from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    image = models.ImageField(
        upload_to='image/',
        blank=True
    )
    name = models.CharField(max_length=50)
    text = models.TextField()
    price = models.FloatField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.text

class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг'
    )

    class Meta:
        ordering = ('-pub_date'),
        verbose_name = 'Комментарий'

    def __str__(self):
        return self.text
