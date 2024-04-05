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

    #tag links
    path('tag/<str:tag>/', views.tag_detail_view, name='tag_detail_view'),

]
