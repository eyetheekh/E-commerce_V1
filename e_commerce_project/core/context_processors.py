from .models import Cart, Category, Order, Product, Vendor, Product_Images, Product_Review


def context_fn(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    context = {
        'categories_context': categories,
        'vendors_context': vendors,
    }

    return context
