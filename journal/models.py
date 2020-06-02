from django.conf import settings
from django.db import models


class Topic(models.Model):
    """New research section"""
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the stream representation of the model"""
        return self.text

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Record(models.Model):
    """"New record"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,  verbose_name='Заголовок')
    comment = models.CharField(max_length=10000, blank=True, verbose_name='Описание')
    file = models.FileField(default='default.png', blank=True, null=True, verbose_name='Файл')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')

    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата')

    def __str__(self):
        """Returns the stream representation of the model"""
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
