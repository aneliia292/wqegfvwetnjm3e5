from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    view = models.CharField(max_length=300)
    price = models.IntegerField()

    def __str__(self):
        return self.name



class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'
