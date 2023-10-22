from django.test import TestCase
class ViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.admin = "http://127.0.0.1:8000/admin/ "
        return super().setUp()
    
    def test_admin_page(self):
        res = self.client.get(self.admin)
        self.assertEqual(res.status_code, 200, "Your admin page has problem, Check Admin views")