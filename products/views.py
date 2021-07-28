from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)