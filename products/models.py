from django.db import models

# Create your models here.

# Modelo de Categorias
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name = 'Nombre')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits= 10, decimal_places=2, verbose_name='Price')
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name