from django.db import models


class Products(models.Model):
    name = models.CharField('Название', max_length=30)
    text = models.TextField('Описание', null=True)
    img = models.ImageField('Изображение', upload_to='mainapp/media/', default='')
    price = models.IntegerField('Цена', null=True)
    show_in_index = models.BooleanField('На главной', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
