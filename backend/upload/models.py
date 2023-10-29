from collections.abc import Iterable
from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
import uuid

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(default="")
    thumb = models.ImageField(null=True, blank=True)

    def delete(self) -> tuple[int, dict[str, int]]:
        if self.thumb:
            self.thumb.storage.delete(self.thumb.name)
        return super().delete()
    
    def save(self, **kw) -> None:
        if self.thumb:
            self.thumb.storage.delete(self.thumb.name)
        return super().save(**kw)
    
    def __str__(self):
        return self.name

class Upload(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(default="",)
    img = models.ImageField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    user = models.ForeignKey(User, related_name="user_product", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="product_catgrory", on_delete=models.CASCADE)
    pic = models.ManyToManyField(Upload, blank=True)
    price = models.FloatField()
    discount = models.IntegerField(default=0)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class UploadSerializer(ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"