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

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        user = UserModel.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
