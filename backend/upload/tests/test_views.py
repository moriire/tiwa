from django.test import TestCase
class ViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.api = "http://127.0.0.1:8000/api/"
        self.category = "http://127.0.0.1:8000/api/category/"
        self.product = "http://127.0.0.1:8000/api/product/"
        self.upload = "http://127.0.0.1:8000/api/upload/"
        self.auth_login = "http://127.0.0.1:8000/auth/login/"
        self.auth_register = "http://127.0.0.1:8000/auth/register/"
        return super().setUp()
    
    def test_auth_login(self):
        res = self.client.get(self.auth_login)
        self.assertEqual(res.status_code, 200, "Your admin page has problem, Check Admin views")

    def test_auth_register(self):
        res = self.client.get(self.auth_register)
        self.assertEqual(res.status_code, 200, "Your admin page has problem, Check Admin views")

    def test_api_page(self):
        res = self.client.get(self.api)
        self.assertEqual(res.status_code, 200, "Your admin page has problem, Check Admin views")

    def test_api_category(self):
        res = self.client.get(self.category)
        self.assertEqual(res.status_code, 200, "Your admin page has problem, Check Admin views")

    def test_api_upload(self):
        res = self.client.get(self.upload)
        self.assertEqual(res.status_code, 200, "Your admin page has problem, Check Admin views")

    def test_api_product(self):
        res = self.client.get(self.product)
        self.assertEqual(res.status_code, 200, "Your admin page has problem, Check Admin views")