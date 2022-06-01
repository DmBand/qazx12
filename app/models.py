from django.db import models


class Data(models.Model):
    """ Модель хранения данных """

    data = models.JSONField(verbose_name='данные')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
