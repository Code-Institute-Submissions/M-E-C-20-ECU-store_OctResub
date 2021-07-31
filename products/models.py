from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    manufacturer = models.CharField(max_length=254)
    model = models.CharField(max_length=254)
    year = models.CharField(max_length=254)
    version = models.CharField(max_length=254)
    enginecode = models.CharField(max_length=254)
    fuel = models.CharField(max_length=254)
    kw = models.CharField(max_length=254)
    ecubrand = models.CharField(max_length=254)
    ecuversion = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.manufacturer
