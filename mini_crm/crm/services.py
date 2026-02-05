from decimal import Decimal
from .models import SizePrice

def normalize_extras(extras):
    return sorted(extras or [])

def calculate_unit_price(product, size_name):
    size = SizePrice.objects.filter(
        product=product,
        size_name=size_name
    ).first()

    price = size.price if size else product.base_price

    if product.offer_percent > 0:
        price = price * (Decimal(1) - Decimal(product.offer_percent) / 100)

    return price


def merge_cart_items(items):
    merged = []

    for item in items:
        item["extras"] = normalize_extras(item.get("extras"))
        found = False

        for m in merged:
            if (
                m["product"] == item["product"]
                and m["size_name"] == item["size_name"]
                and m["extras"] == item["extras"]
                and m["customization"] == item["customization"]
            ):
                m["qty"] += item["qty"]
                found = True
                break

        if not found:
            merged.append(item)

    return merged
