from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=30)
    img = models.ImageField('Изображение', upload_to='mainapp/media/categories', default='')
    show = models.BooleanField('На главной', default=True)
    priority = models.IntegerField('Приоритет', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField('Название', max_length=60)
    img = models.ImageField('Изображение', upload_to='mainapp/media', default='')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Price(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField('Цена', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Edges(models.Model):
    text = models.TextField('Текст')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Плюс'
        verbose_name_plural = 'Плюсы'


class Cares(models.Model):
    name = models.CharField('Название', max_length=30)
    text = models.TextField('Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уход'
        verbose_name_plural = 'Уходы'
