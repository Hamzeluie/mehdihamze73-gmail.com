from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import UserProfile


class UserProfileSerializer(ModelSerializer):
    # name = serializers.CharField(max_length=200)
    # email = serializers.CharField(max_length=255)
    # password = serializers.CharField(max_length=255)
    class Meta:
        model = UserProfile
        fields = ('id',
                  'name',
                  'email',
                  'is_active',
                  'password',
                  'is_superuser',
                  )
        extra_kwargs = {
                'password': {
                    'write_only': True,
                    'style': {'input_type': 'password'}
                             }
            }

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
