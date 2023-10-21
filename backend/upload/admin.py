from django.contrib import admin
from .models import Upload, Category, Product
admin.site.register(Category)
admin.site.register(Upload)
admin.site.register(Product)