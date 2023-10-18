from django.db import models
from django.contrib.auth import get_user_model
from upload.models import Product 
User = get_user_model()
class Order(models.Model):
    user = models.ForeignKey(User, related_name="user_order", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="ordered_product", on_delete=models.DO_NOTHING)
    ordered_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)