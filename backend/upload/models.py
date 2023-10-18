from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
User = get_user_model()
class Upload(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(default="")
    img = models.ImageField()

    def __init__(self):
        return self.name
    
class Product(models.Model):
    user = models.ForeignKey(User, related_name="user_product", on_delete=models.CASCADE)
    pic = models.ManyToManyField(Upload, blank=True)
    price = models.FloatField()
    discount = models.IntegerField(default=0)

class UploadSerializer(ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"