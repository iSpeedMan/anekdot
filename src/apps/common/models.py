from django.db import models

def common_img_name(instance, filename):
    return 'common/{0}/img/{1}'.format(instance.name, filename)

class Common(models.Model):
    name = models.CharField('Название рецепта', max_length=100)
    text = models.TextField('Приготовление')
    img = models.ImageField('Изоброжение блюда', upload_to=common_img_name, help_text='Изоброжение блюда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

