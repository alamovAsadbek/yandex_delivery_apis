from django.db import models
from django.contrib.auth import get_user_model

from app_common.models import BaseModel
from app_products.models import ProductsModel

User = get_user_model()


class OrderStatus(models.TextChoices):
    PENDING_COURIER = 'pending_for_courier', 'Pending for a Courier'
    PENDING_RESTAURANT = 'pending_for_restaurant', 'Pending for a Restaurant'
    CONFIRMED_COURIER = 'confirmed_by_courier', 'Confirmed by a Courier'
    CONFIRMED_RESTAURANT = 'confirmed_by_restaurant', 'Confirmed by a Restaurant'
    DELIVERING = 'delivering', 'Delivering'
    DELIVERED = 'delivered', 'Delivered'
    CANCELLED = 'cancelled', 'Cancelled'


class OrderItemModel(models.Model):
    product = models.ForeignKey(
        ProductsModel,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name='Product'
    )
    quantity = models.PositiveIntegerField(default=1)
    price_per_item = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'


class OrderModel(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='User'
    )
    order_status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING_COURIER,
        verbose_name='Order Status'
    )
    order_items = models.ManyToManyField(
        OrderItemModel,
        related_name='orders',
        verbose_name='Order Items'
    )

    def __str__(self):
        return f"Order #{self.pk} | User: {self.user.phone_number}"

    @property
    def items(self):
        return self.order_items.all()

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items)

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
