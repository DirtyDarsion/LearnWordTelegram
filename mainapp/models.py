from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField('Название', max_length=30)
    text = models.TextField('Описание', blank=True)
    img = models.ImageField('Изображение', upload_to='mainapp/media/', default='')
    price = models.IntegerField('Цена', blank=True, default=0)
    show_in_index = models.BooleanField('На главной', default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
