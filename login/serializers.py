from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import UserProfile


class UserProfileSerializer(ModelSerializer):
    # name = serializers.CharField(max_length=200)
    # email = serializers.CharField(max_length=255)
    # password = serializers.CharField(max_length=255)
    class Meta:
        model = UserProfile
        fields = ('name',
                  'email',
                  'password'
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
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
