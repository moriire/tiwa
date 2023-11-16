from collections.abc import Iterable
from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
import uuid
User = get_user_model()

def upload_location(instance, filename):
    y = "_".join(instance.product.name.split(" "))
    return f"products/{y}/{filename}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(default="")
    thumb = models.ImageField(null=True, blank=True)

    def delete(self) -> tuple[int, dict[str, int]]:
        if self.thumb:
            self.thumb.storage.delete(self.thumb.name)
        return super().delete()
    """
    def save(self, **kw) -> None:
        if self.thumb:
            self.thumb.storage.delete(self.thumb.name)
        return super().save(**kw)
    """
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    user = models.ForeignKey(User, related_name="user_product", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="product_catgrory", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    price = models.FloatField()
    discount = models.IntegerField(default=0)

class Upload(models.Model):
    product = models.ForeignKey(Product, related_name="product_upload", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(upload_to=upload_location)

    def __str__(self):
        return self.name
    
class ProductWithImages(models.Model):
    product = models.ForeignKey(Product, related_name="product_with_images_upload", on_delete=models.CASCADE, null=True, blank=True)
    images = models.ManyToManyField(Upload, related_name="product_with_images")

    def __str__(self):
        return self.product

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryNameSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)

class UploadSerializer(ModelSerializer):
    class Meta:
        model = Upload
        fields = ("img", "product",)

class SingleImageUploadSerializer(ModelSerializer):
    class Meta:
        model = Upload
        fields = ("img",)

class FullProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    category = CategoryNameSerializer()
    class Meta:
        model = Product
        fields = "__all__"

class ProductWithImagesSerializer(ModelSerializer):
    product = ProductSerializer()
    images = UploadSerializer(many=True)
    class Meta:
        model = ProductWithImages
        fields = "__all__"