from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from upload.models import (
    Category,
    Upload,
    Product,
    CategorySerializer,
    UploadSerializer,
    ProductSerializer
)

class CategoryAPITestCase(APITestCase):
    def setUpCategory(self):
        self.category_data = {
            'name': 'African Art', 
            'desc': 'African Art African Art African Art African Art African Art African Art',
        }
        self.category = Category.objects.create(**self.category_data)


    def setUpProduct(self):
        self.product_data = {
            "price": 3000,
            "discount": 10,
            "user": 1,
            "category": self.category,
        }
        self.product = Product.objects.create(**self.product_data)

    def test_get_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, CategorySerializer(self.category).data)

    def test_get_product(self):
        url = reverse('product-detail', kwargs={'pk': self.prodcut.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ProductSerializer(self.product).data)

    def test_create_category(self):
        data = {
            'name': 'African Cultural Wears', 
            'desc': 'African Cultural Wears African Cultural Wears African Cultural Wears Art African Art African Art African Art',
        }
        response = self.client.post(reverse('category-list'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)  # Assuming you had only one object before

    def test_create_product(self):
        data = {
            'name': 'African Cultural Wears', 
            'desc': 'African Cultural Wears African Cultural Wears African Cultural Wears Art African Art African Art African Art',
        }
        response = self.client.post(reverse('product-list'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)  # Assuming you had only one object before

    def test_update_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        data = {'name': 'testing'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'testing')

    def test_delete_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    
    def test_update_product(self):
        url = reverse('product-detail', kwargs={'pk': self.category.id})
        data = {'name': 'testing'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'testing')

    def test_delete_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)