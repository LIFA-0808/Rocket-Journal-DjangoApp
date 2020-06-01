from django.db import models


class Topic(models.Model):
    """New research section"""
    text = models.CharField(max_length=200)
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
    text = models.CharField(max_length=100,  verbose_name='Заголовок')
    comment = models.CharField(max_length=15000, blank=True, verbose_name='Описание')
    image = models.FileField(default='default.png', blank=True, null=True, verbose_name='Файл')
    # author = model.CharField(max_length=100, default=user.username, verbose_name='Автор')

    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата')

    def __str__(self):
        """Returns the stream representation of the model"""
        return f"{self.date_added} - {self.topic}"

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
