from django.shortcuts import render
from django.contrib import messages
from .models import Cart, Category, Order, Product, Vendor, Product_Images, Product_Review


def home(request):

    feartured_products = Product.objects.filter(featured_on_home_page=True)
    latest_products = Product.objects.filter().order_by('-date_added')[:4]

    context = {
        "feartured_products": feartured_products,
        'latest_products': latest_products,
    }
    return render(request, 'core/index.html', context)
