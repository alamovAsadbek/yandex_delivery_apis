from rest_framework import serializers

from .models import UserModel


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}
        username_field = 'phone_number'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        print(validated_data['phone_number'])
        phone_number = validated_data['phone_number']
        username = phone_number
        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        if not phone_number:
            raise serializers.ValidationError({'phone_number': 'This field is required.'})

        # Check if phone number already exists
        if UserModel.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'phone_number': 'This phone number is already registered.'})

        # Create the user
        validated_data['username'] = username
        user = UserModel.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
