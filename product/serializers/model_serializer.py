from rest_framework import serializers
from ..models import CarModel
from ..models import Product
from .product_serializer import ProductSerializer

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= CarModel
        fields='__all__'
    def create(self, validated_data):
        products = validated_data.pop('products')
        model = CarModel.objects.create(**validated_data)
        for product in products:
            Product.objects.create(CarModel=model, **product)
        return model