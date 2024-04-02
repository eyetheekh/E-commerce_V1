from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid




# class Category(models.Model):
#     category_id = models.UUIDField(
#         primary_key=True, default=uuid.uuid4, editable=False)
#     title = models.CharField(max_length=100)
#     desc = models.CharField(max_length=500)
#     image=models.ImageField(upload_to='Category_images')

# class Product(models.Model):
#     product_id = models.UUIDField(
#         primary_key=True, default=uuid.uuid4, editable=False)
#     title = models.CharField(max_length=100)
#     desc = models.CharField(max_length=500)
#     category = models.ForeignKey(
#         Category, on_delete=models.CASCADE, related_name='product_category')
#     image=models.ImageField(upload_to='Product_images')
#     stock=models.IntegerField(default=100)

