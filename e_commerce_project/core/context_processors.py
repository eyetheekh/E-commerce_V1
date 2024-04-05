from .models import Cart, Category, Order, Product, Vendor, Product_Images, Product_Review


def context_fn(request):
    categories = Category.objects.all()
    context = {
        'categories_context': categories,
    }

    return context
