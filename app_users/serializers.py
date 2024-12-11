from rest_framework import serializers

from .models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    """
    Serializer for UserModel. It includes the create method to create a new user.
    """

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}
        username_field = 'phone_number'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        phone_number = validated_data['phone_number']
        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        if not phone_number:
            raise serializers.ValidationError({'phone_number': 'This field is required.'})

        # Check if phone number already exists
        if UserModel.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'phone_number': 'This phone number is already registered.'})
        elif UserModel.objects.filter(username=phone_number).exists():
            raise serializers.ValidationError({'phone_number': 'This phone number is already registered.'})

        # Create the user
        validated_data['username'] = validated_data.pop('phone_number')
        user = UserModel.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('Phone number must be a number.')
        elif UserModel.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError('This phone number is already registered.')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        elif not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Password must contain at least one digit.')
        elif not any(char.isalpha() for char in value):
            raise serializers.ValidationError('Password must contain at least one letter.')
        return value


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer for login. It includes the fields for phone_number and password.
    """
    phone_number = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['phone_number', 'password']


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for changing password. It includes the fields for old_password, new_password, and confirm_password.
    """
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['old_password', 'new_password', 'confirm_password']

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect.')
        return value

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        elif not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Password must contain at least one digit.')
        elif not any(char.isalpha() for char in value):
            raise serializers.ValidationError('Password must contain at least one letter.')
        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'Passwords do not match.'})
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
