from django.db import models


class Product(models.Model):
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
    sku = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.manufacturer
