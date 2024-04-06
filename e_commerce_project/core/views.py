from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cart, Category, Order, Product, Vendor, Product_Images, Product_Review
from taggit.models import Tag
from .forms import Product_Review_Form
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string


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


# def add_to_cart(request):
#     id = request.GET['id']
#     product = get_object_or_404(Product, id=id)

#     cart_product = {}
#     cart_product[id] = {

#         'title': product.title,
#         'quantity': request.GET['quantity'],
#         'price': str(product.price_after_discount()),
#     }

#     print(cart_product)

#     if 'cart_data_object' in request.session:
#         if id in request.session['cart_data_object']:
#             cart_data = request.session['cart_data_object']
#             cart_data[id]["quantity"] = cart_product[id]["quantity"]
#             cart_data.update(cart_data)
#             request.session['cart_data_object'] = cart_data
#         else:
#             cart_data = request.session['cart_data_object']
#             cart_data.update(cart_product)
#             request.session['cart_data_object'] = cart_data
#     else:
#         request.session['cart_data_object'] = cart_product

#     print(request.session['cart_data_object'])

#     return JsonResponse({
#         "data": request.session['cart_data_object'],
#         "no_of_cart_items": len(request.session['cart_data_object']),
#         "boolean": True
#     })
def add_to_cart(request):
    id = request.GET['id']
    product = get_object_or_404(Product, id=id)
    quantity = int(request.GET['quantity'])

    cart_product = {
        'title': product.title,
        'quantity': quantity,
        'price': str(product.price_after_discount()),
    }

    # print(cart_product)

    if 'cart_data_object' in request.session:
        cart_data = request.session['cart_data_object']
        if id in cart_data:
            # If product already exists in cart, increment the quantity
            # cart_data[id]["quantity"] += int(quantity)
            cart_data[id]["quantity"] = int(
                cart_data[id]["quantity"]) + quantity

        else:
            # If product doesn't exist in cart, add it
            cart_data[id] = cart_product
        request.session['cart_data_object'] = cart_data
    else:
        request.session['cart_data_object'] = {id: cart_product}

    # print(request.session['cart_data_object'])

    return JsonResponse({
        "data": request.session['cart_data_object'],
        "no_of_cart_items": len(request.session['cart_data_object']),
        "boolean": True
    })


def cart_view(request):
    list_of_products_in_cart = list()

    if 'cart_data_object' not in request.session:
        messages.warning(
            request, 'Your Cart is empty, Add items to Your Cart!')
        return redirect('core:home')

    else:
        # print(request.session['cart_data_object'])
        id_of_products = [i for i in request.session['cart_data_object']]

        list_of_products_in_cart = [
            Product.objects.get(id=i) for i in id_of_products]
        # print(list_of_products_in_cart)

        cart_dict = dict()

        for i in list_of_products_in_cart:
            cart_dict[i] = request.session['cart_data_object'][str(
                i.id)]['quantity']

        # print('cart_dict: ', cart_dict)

        cart_dict_with_price_and_qty = dict()
        for i, j in cart_dict.items():
            # print(i, j)
            cart_dict_with_price_and_qty[i] = {
                "quantity": j,
                "sub_total": i.price_after_discount() * int(j)
            }

        # print('cart____', cart_dict_with_price_and_qty)

        cart_total = 0
        for i, j in cart_dict_with_price_and_qty.items():
            # print(i, j)
            cart_total += j['sub_total']

        total_cart_items = len(list_of_products_in_cart)

    context = {
        'total_cart_items': total_cart_items,
        'cart_dict_with_price_and_qty': cart_dict_with_price_and_qty,
        'cart_total': cart_total,
    }
    return render(request, 'core/cart.html', context)


def delete_product_from_cart(request):
    id = request.GET['id']
    # print(id)

    temp_dict = request.session['cart_data_object']
    temp_dict.pop(id)
    request.session['cart_data_object'] = temp_dict

    ####################################################

    id_of_products = [i for i in request.session['cart_data_object']]

    list_of_products_in_cart = [
        Product.objects.get(id=i) for i in id_of_products]
    # print(list_of_products_in_cart)

    cart_dict = dict()

    for i in list_of_products_in_cart:
        cart_dict[i] = request.session['cart_data_object'][str(
            i.id)]['quantity']

    # print('cart_dict: ', cart_dict)

    cart_dict_with_price_and_qty = dict()
    for i, j in cart_dict.items():
        # print(i, j)
        cart_dict_with_price_and_qty[i] = {"quantity": j,
                                           "sub_total": i.price_after_discount() * int(j)}

    # print('cart____', cart_dict_with_price_and_qty)

    cart_total = 0
    for i, j in cart_dict_with_price_and_qty.items():
        # print(i, j)
        cart_total += j['sub_total']

    total_cart_items = len(list_of_products_in_cart)

    context = render_to_string('core/async/cart_async.html', {
        'total_cart_items': total_cart_items,
        'cart_dict_with_price_and_qty': cart_dict_with_price_and_qty,
        'cart_total': cart_total,
    })

    return JsonResponse({
        'context': context,
        'total_cart_items': total_cart_items
    })


def update_from_cart(request):
    id = request.GET.get('id')
    quantity = request.GET['quantity']

    temp_dict = request.session['cart_data_object']
    print(temp_dict[id])
    temp_dict[id]['quantity'] = quantity
    request.session['cart_data_object'] = temp_dict

    ####################################################

    id_of_products = [i for i in request.session['cart_data_object']]

    list_of_products_in_cart = [
        Product.objects.get(id=i) for i in id_of_products]
    # print(list_of_products_in_cart)

    cart_dict = dict()

    for i in list_of_products_in_cart:
        cart_dict[i] = request.session['cart_data_object'][str(
            i.id)]['quantity']

    # # print('cart_dict: ', cart_dict)

    cart_dict_with_price_and_qty = dict()
    for i, j in cart_dict.items():
        # print(i, j)
        cart_dict_with_price_and_qty[i] = {"quantity": j,
                                           "sub_total": i.price_after_discount() * int(j)}

    # # print('cart____', cart_dict_with_price_and_qty)

    cart_total = 0
    for i, j in cart_dict_with_price_and_qty.items():
        # print(i, j)
        cart_total += j['sub_total']

    total_cart_items = len(list_of_products_in_cart)

    context = render_to_string('core/async/cart_async.html', {
        'total_cart_items': total_cart_items,
        'cart_dict_with_price_and_qty': cart_dict_with_price_and_qty,
        'cart_total': cart_total,
    })

    return JsonResponse({
        'context': context,
        'total_cart_items': total_cart_items,
        "bool": True
    })


def checkout_view(request):
    return render(request, 'core/')
