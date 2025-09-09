from rest_framework import serializers
from .models import Advertisment

class advertismentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Advertisment
        fields='__all__'