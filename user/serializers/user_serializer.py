from rest_framework import serializers
from ..models import User
from django.contrib.auth.models import User, Permission
class UserSerializer(serializers.Serializer):
    id= serializers.UUIDField(
        read_only= True
    )
    username= serializers.CharField()
    password= serializers.CharField()
    permissions = serializers.ListField(write_only= True)

    def create(self, validated_data:dict):
        permission = validated_data.pop('permissions')
        user= User.objects.create_user(**validated_data)
        user.user_permissions.set(permission)
        return user
    
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields='__all__'
