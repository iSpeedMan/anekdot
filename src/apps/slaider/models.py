from django.db import models
from django.shortcuts import reverse


def poster_img_name(instance, filename):
    return 'mems/{0}/img/{1}'.format(instance.name, filename)


class Mems(models.Model):
    name = models.CharField('Имя мема', max_length=100)
    img = models.ImageField('Изоброжение мема', upload_to=poster_img_name, help_text='700x200px')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мем'
        verbose_name_plural = 'Мемы'

