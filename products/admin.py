from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'manufacturer',
        'model',
        'year',
        'version',
        'enginecode',
        'fuel',
        'kw',
        'ecubrand',
        'ecuversion',
        'price',
        'sku',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
