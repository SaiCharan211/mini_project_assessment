from django.db import models
from django.utils import timezone
import uuid

class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    gst_no = models.CharField(max_length=50, blank=True)


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("email", "organization")


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_percent = models.PositiveIntegerField(default=0)


class SizePrice(models.Model):
    product = models.ForeignKey(Product, related_name="sizes", on_delete=models.CASCADE)
    size_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Order(models.Model):
    order_no = models.CharField(max_length=50, unique=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    @staticmethod
    def generate_order_no():
        return f"ORD-{timezone.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:4]}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    size_name = models.CharField(max_length=50)
    qty = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)
    extras = models.JSONField(default=list)
    customization = models.TextField(blank=True)
