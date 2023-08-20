from django.db import models
from django.contrib.auth.models import User


class New(models.Model):

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField('статья')
    data_pub = models.DateTimeField(auto_now_add=True)
    category = models.SlugField('Category', max_length=10, choices=models.CASCADE,)


    def preview(self):
        preview = f'{self.text[:128]}...'
        return preview

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



    def __str__(self):
        return f'{self.title}'


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )

