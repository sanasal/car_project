from rest_framework import serializers
from .models import advertisment

class advertismentSerializer(serializers.ModelSerializer):
    class Meta:
        model= advertisment
        fields='__all__'