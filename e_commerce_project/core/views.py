from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cart, Category, Order, Product, Vendor, Product_Images, Product_Review
from taggit.models import Tag


def home(request):

    feartured_products = Product.objects.filter(featured_on_home_page=True)
    latest_products = Product.objects.filter().order_by('-date_added')[:4]

    context = {
        "feartured_products": feartured_products,
        'latest_products': latest_products,
    }
    return render(request, 'core/index.html', context)


def product_detail_view(request, PID):
    product = get_object_or_404(Product, PID=PID)
    related_products = Product.objects.filter(category=product.category)
    print(product.discount_percentage())

    context = {
        "product": product,
        "related_products": related_products,
    }
    return render(request, 'core/product_detail_view.html', context)


def category_detail_view(request, CID):
    category = get_object_or_404(Category, CID=CID)
    products_in_category = Product.objects.filter(category=category)
    context = {
        'products_in_category': products_in_category,
        'category': category,
    }
    return render(request, 'core/category_view.html', context)


def category_list_view(request):
    all_categories = Category.objects.all()

    context = {
        'all_categories': all_categories,
    }
    return render(request, 'core/all_categories.html', context)


def vendor_detail_view(request, VID):
    vendor = get_object_or_404(Vendor, VID=VID)
    products_of_vendor = Product.objects.filter(vendor=vendor)

    context = {
        'vendor': vendor,
        'products_of_vendor': products_of_vendor
    }
    return render(request, 'core/vendor_details.html', context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()

    context = {
        'vendors': vendors
    }
    return render(request, 'core/vendor_list.html', context)


def vendor_shop_view(request, VID):
    vendor = get_object_or_404(Vendor, VID=VID)
    products_of_vendor = Product.objects.filter(vendor=vendor)

    context = {
        'vendor': vendor,
        'products_of_vendor': products_of_vendor
    }
    return render(request, 'core/vendor_shop.html', context)


def tag_detail_view(request, tag):
    tag = get_object_or_404(Tag, name=tag)
    tag_products = Product.objects.filter(tags=tag)

    context = {
        'tag_products': tag_products,
        'tag': tag,
    }
    return render(request, 'core/tag.html', context)
