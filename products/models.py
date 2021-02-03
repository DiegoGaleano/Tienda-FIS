from django.db import models
from django.utils.timezone import now
# Create your models here.

class Category(models.Model):
	'Categoria productos'
	name = models.CharField(max_length=200, verbose_name='Nombre Categoría')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Actualización')

	class Meta:
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'
		ordering = ['-created', 'name']

	def __str__(self):
		return self.name


class Product(models.Model):
    '''
    Modelo de productos
    '''
    name = models.CharField(max_length=100, verbose_name='Nombre producto')
    description = models.TextField(blank = True, verbose_name='Descripción producto')
    price = models.IntegerField(verbose_name='Precio')
    quantity = models.IntegerField(verbose_name='Cantidad')

    picture = models.ImageField(
        upload_to = 'products/picture',
        blank = True,
        null = True
    )
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_products')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name='Product'
        verbose_name_plural = 'Product'
        ordering = ['-created', 'name']

    def __str__(self):
        return self.name


