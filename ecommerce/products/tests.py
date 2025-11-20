from django.test import TestCase
from django.urls import reverse
from .models import Product, Category

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")
        self.assertTrue(isinstance(self.category, Category))

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Books")
        self.product = Product.objects.create(
            name="Django for Beginners",
            category=self.category,
            price=29.99,
            description="A beginner-friendly Django book"
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Django for Beginners")
        self.assertEqual(self.product.category.name, "Books")
        self.assertTrue(isinstance(self.product, Product))

class ViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Toys")
        self.product = Product.objects.create(
            name="Toy Car",
            category=self.category,
            price=9.99,
            description="A small toy car"
        )

    def test_home_view(self):
        response = self.client.get(reverse('products:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/home.html')

    def test_category_list_view(self):
        response = self.client.get(reverse('products:category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Toys")

    def test_list_products_view(self):
        response = self.client.get(reverse('products:list_products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Toy Car")
