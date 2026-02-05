from rest_framework import serializers
from .models import *

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class SizePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizePrice
        fields = "__all__"
