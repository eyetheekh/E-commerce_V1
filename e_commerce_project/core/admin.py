from django.contrib import admin

from .models import Cart, Category, Order, Product, Vendor, Product_Images, Product_Review


class ProductImagesAdmin(admin.TabularInline):
    model = Product_Images


class Product_Admin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['title', 'category', 'vendor', 'price', 'discount_amount', 'tags',
                    'product_status', 'featured_on_home_page',]
    list_editable = ['category', 'vendor', 'product_status', 'price',
                     'discount_amount', 'tags', 'featured_on_home_page',]


admin.site.register(Product, Product_Admin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Vendor)
admin.site.register(Product_Images)
admin.site.register(Product_Review)
