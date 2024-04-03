from django.contrib import admin

from .models import Cart, Category, Order, Product, Vendor, Product_Images, Product_Review


class Product_Admin(admin.ModelAdmin):
    list_display = ['PID', 'title', 'category', 'price', 'discount_amount',
                    'product_status', 'featured_on_home_page',]
    list_editable = ['category', 'product_status', 'price',
                     'discount_amount', 'featured_on_home_page',]


admin.site.register(Product, Product_Admin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Vendor)
admin.site.register(Product_Images)
admin.site.register(Product_Review)
