from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    # img_url = models.ImageField(upload_to='mainapp/media/products/', width_field=None)
    price = models.IntegerField(default=True)

    def __str__(self):
        return self.name
