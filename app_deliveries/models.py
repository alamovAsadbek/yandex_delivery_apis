from django.db import models
from django.contrib.auth import get_user_model

from app_basket.models import BasketModel
from app_branch.models import BranchModel
from app_common.models import BaseModel
from app_company.models import RestaurantModel
from app_products.models import ProductsModel
from app_users.models import UserLocations

User = get_user_model()


class OrderStatus(models.TextChoices):
    """
    OrderStatus is a class that contains choices for the order status.
    """
    PENDING_COURIER = 'pending_for_courier', 'Pending for a Courier'
    PENDING_RESTAURANT = 'pending_for_restaurant', 'Pending for a Restaurant'
    CONFIRMED_RESTAURANT = 'confirmed_by_restaurant', 'Confirmed by a Restaurant'
    DELIVERING = 'delivering', 'Delivering'
    DELIVERED = 'delivered', 'Delivered'
    CANCELLED = 'cancelled', 'Cancelled'


class OrderItemModel(models.Model):
    """
    OrderItem model represents an item in an order.
    product: The product associated with the order item.
    quantity: The quantity of the product ordered.
    price_per_item: The price per unit of the product.
    total_price: The total price for the order item.
    """
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
    """
    Order model represents an order placed by a user in the application.
    restaurant: The restaurant where the order is placed.
    branch: The branch where the order is placed.
    user: The user who placed the order.
    courier: The courier assigned to the order.
    order_status: The status of the order being placed.
    order_items: The items in the order.
    delivery_address: The address where the order is to be delivered.
    """
    restaurant = models.ForeignKey(
        RestaurantModel,
        on_delete=models.SET_NULL,
        related_name='orders',
        verbose_name='Restaurant',
        null=True
    )
    branch = models.ForeignKey(
        BranchModel,
        on_delete=models.SET_NULL,
        related_name='orders',
        verbose_name='Branch',
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='User'
    )
    courier = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='orders',
        verbose_name='Courier'
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
    delivery_address = models.ForeignKey(
        UserLocations,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Delivery Address'
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
