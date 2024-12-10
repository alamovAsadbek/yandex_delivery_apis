from rest_framework import serializers

from app_basket.models import BasketModel
from app_deliveries.models import OrderModel, OrderItemModel


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for OrderModel.
    """
    class Meta:
        model = OrderModel
        fields = '__all__'
        read_only_fields = ['id', 'user', 'courier', 'order_status', 'order_items']

    def create(self, validated_data):
        """
        Create a new order with the provided data.
        """
        basket = validated_data.pop('basket')
        order = OrderModel.objects.create(**validated_data)
        for item in basket.items.all():
            # Create an order item for each item in the basket
            item_data = dict()
            item_data['price_per_item'] = item.product.price
            item_data['quantity'] = item.quantity
            item_data['total_price'] = item.product.price * item.quantity
            # Create an order item for each item in the basket and add it to the order
            order_item = OrderItemModel.objects.create(order=order, **item_data)
            order.items.add(order_item)
            # Remove the item from the basket
            basket.items.remove(item)
            basket.save()
        order.save()
        return order

    def update(self, instance, validated_data):
        """
        Update an existing order with the provided data.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate(self, attrs):
        """
        Validate the order data.
        """
        # Check if the basket exists and is not empty
        basket = attrs.get('basket')
        if not basket or not basket.items.all():
            raise serializers.ValidationError('Basket must not be empty.')
        return attrs

    def to_representation(self, instance):
        """
        Customize the representation of the order data.
        """
        # Add the total items and total price to the representation
        representation = super().to_representation(instance)
        representation['total_items'] = instance.total_items
        representation['total_price'] = instance.total_price
        return representation
