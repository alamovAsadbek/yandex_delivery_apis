from rest_framework import serializers

from .models import ProductsModel


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = ProductsModel
        fields = ('id', 'name', 'price', 'description', 'restaurant', 'status')
