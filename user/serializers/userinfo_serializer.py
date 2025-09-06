from rest_framework import serializers
from ..models import Userinfo

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Userinfo
        fields='__all__'