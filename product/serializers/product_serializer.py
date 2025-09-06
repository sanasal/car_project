from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models import Product, CarModel

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= CarModel
        fields='__all__'


class ProductSerializer(serializers.Serializer):
    id= serializers.UUIDField(
        read_only= True
    )
    license_plate = serializers.CharField(
        max_length= 20,
        min_length= 10 ,
        validators= [
            UniqueValidator(
                queryset= Product.objects.all()
            )
        ],
    )
    features= serializers.CharField(
        max_length= 4000
    )
    is_new= serializers.BooleanField()
    current_kilometer= serializers.IntegerField()
    created_at= serializers.DateTimeField(
        read_only= True
    )
    updated_at= serializers.DateTimeField(
        read_only= True
    )
    engine = serializers.IntegerField()
    is_deleted= serializers.BooleanField()
    CarModel= serializers.PrimaryKeyRelatedField(
        queryset= CarModel.objects.all(),
        required= False
        
    )
    model_name = serializers.CharField(
        read_only= True,
        source = "CarModel.name"
    )
    model_details= ModelSerializer(source= "CarModel", read_only= True)
    price= serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(
            **validated_data
        )
    
    def update(self, instance:Product, validated_data:dict):
        instance.license_plate = validated_data.get('license_plate', instance.license_plate)
        instance.is_new = validated_data('is_new', instance.is_new)
        instance.save()
        return instance

