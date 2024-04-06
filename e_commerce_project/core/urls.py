from django.urls import path
from .import views
app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<PID>/', views.product_detail_view, name='product_detail_view'),
    path('category/<CID>/', views.category_detail_view,
         name='category_detail_view'),
    path('categories/', views.category_list_view, name='category_list_view'),

    path('vendor/<VID>/', views.vendor_detail_view, name='vendor_detail_view'),
    path('vendors/', views.vendor_list_view, name='vendor_list_view'),
    path('shop/vendors/<VID>/', views.vendor_shop_view, name='vendor_shop_view'),

    # tag links
    path('tag/<str:tag>/', views.tag_detail_view, name='tag_detail_view'),
    # search
    path('search/', views.search, name='search'),

    # ajax- add to cart
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),

    # cart view
    path('cart/', views.cart_view, name='cart_view'),

    # ajax- del product from cart
    path('del-product-from-cart/', views.delete_product_from_cart,
         name='delete_product_from_cart'),

    # ajax update from cart
    path('update-from-cart/', views.update_from_cart, name='update_from_cart'),

]
