from django.db import models
from django.shortcuts import reverse


class Anekdot(models.Model):
    name = models.CharField('Имя анекдота', max_length=100)
    text = models.TextField('Содержание анекдота')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Анекдот'
        verbose_name_plural = 'Анекдоты'

