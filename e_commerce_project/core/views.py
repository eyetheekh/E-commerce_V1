from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cart, Category, Order, Product, Vendor, Product_Images, Product_Review
from taggit.models import Tag
from .forms import Product_Review_Form
from django.db.models import Q


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

    if request.method == "POST":
        Product_Review.objects.create(
            review=request.POST['review'],
            rating=request.POST['rating'],
            user=request.user,
            product=product,
        )
        messages.success(request, 'Review Added')

        # messages.error(request, 'Review cannot be added')

    reviews_of_product = Product_Review.objects.filter(product=product)
    related_products = Product.objects.filter(
        category=product.category).exclude(PID=product.PID)

    can_review = True
    if request.user.is_authenticated:
        user_reviews = Product_Review.objects.filter(
            product=product, user=request.user)

        if len(user_reviews) > 0:
            can_review = False

    form = Product_Review_Form()

    context = {
        'product': product,
        "related_products": related_products,
        'reviews_of_product': reviews_of_product,
        'can_review': can_review,
        'form': form,
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
    return render(request, 'core/tag_detail_view.html', context)


def search(request):
    query = request.GET.get('q')
    products = None  # Initialize as empty queryset

    if len(query) > 0:
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(desc__icontains=query))

    context = {
        'query': query,
        'products': products
    }

    return render(request, 'core/search.html', context)
