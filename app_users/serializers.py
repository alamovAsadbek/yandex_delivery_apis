from rest_framework import serializers
from .models import UserModel


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}
        username_field = 'phone_number'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        username = validated_data.pop('phone_number', None)

        if not username:
            raise serializers.ValidationError({'phone_number': 'Phone number is required.'})

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        # Check if phone number already exists
        if UserModel.objects.filter(phone_number=username).exists():
            raise serializers.ValidationError({'phone_number': 'This phone number is already registered.'})

        # Add phone_number as username
        validated_data['username'] = username

        # Create the user
        user = UserModel.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
