from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Category, CategorySerializer, Upload, Product, UploadSerializer, ProductSerializer, ProductWithImages, ProductWithImagesSerializer
from rest_framework.decorators import action

class CategoryViews(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UploadViews(ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

class ProductViews(ModelViewSet):
    queryset = Product.objects.all().select_related("category")
    serializer_class = ProductSerializer

class ProductWithImagesViews(ModelViewSet):
    queryset = ProductWithImages.objects.all().prefetch_related("images").select_related("product")
    serializer_class = ProductWithImagesSerializer

    def list(self, request):
        items = self.get_queryset()
        params = request.query_params
        pp = params.dict()
        if params:
            items = items.filter(**pp)
        ser = self.get_serializer(items, many=True)
        return Response(
             	ser.data
                )