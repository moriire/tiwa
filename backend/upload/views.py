from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, CategorySerializer, Upload, Product, UploadSerializer, ProductSerializer

class CategoryViews(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UploadViews(ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

class ProductViews(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer