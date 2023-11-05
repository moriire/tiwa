from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Category, CategorySerializer, Upload, Product, UploadSerializer, ProductSerializer
from rest_framework.decorators import action

class CategoryViews(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UploadViews(ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

    def create(self, request, *args, **kwargs):
        print(args, kwargs)
        return Response({}) #super().create(request, *args, **kwargs)
    

class ProductViews(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["get"])
    def product_per_image(self, request):
        products = self.get_object()
