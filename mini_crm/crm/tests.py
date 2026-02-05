from django.test import TestCase
from .models import *
from .services import calculate_price

class PricingTest(TestCase):
    def test_offer_applied(self):
        p = Product.objects.create(
            name="Test",
            sku="SKU1",
            base_price=100,
            offer_percent=10
        )
        unit, total = calculate_price(p, "M", 2)
        self.assertEqual(float(unit), 90.0)
        self.assertEqual(float(total), 180.0)
