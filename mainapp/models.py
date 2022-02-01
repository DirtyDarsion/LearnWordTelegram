from django.db import models


class Products(models.Model):
    name = models.CharField('Название', max_length=30)
    text = models.TextField('Описание')
    img = models.ImageField('Изображение', upload_to='mainapp/media/', default='')
    price = models.IntegerField('Цена', default=True)
    show_in_index = models.BooleanField('Отображать на главной странице', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
