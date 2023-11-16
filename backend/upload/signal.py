from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Upload, Product, ProductWithImages

@receiver(post_save, sender=Product)
def create_product(sender, instance, **kwargs):
    product = ProductWithImages(product = instance)
    product.save()

@receiver(post_save, sender=Upload)
def update_product(sender, instance, **kwargs):
    product = ProductWithImages.objects.get(product = instance.product)
    product.images.add(instance)
