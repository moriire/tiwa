from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Upload, Product, UploadSerializer, ProductSerializer

class UploadViews(ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer


class ProductViews(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer