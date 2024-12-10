from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app_common.premissions import IsCourier
from app_deliveries.models import OrderModel, OrderStatus
from app_deliveries.serializers import OrderSerializer


class MyDeliveredDeliveries(generics.ListAPIView):
    """
    Retrieve a list of delivered deliveries for a specific user.
    """
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsCourier]

    def get_queryset(self):
        return self.queryset.filter(courier=self.request.user)

    def get_paginated_response(self, data):
        print(data)
        return Response({
            'results': data
        })


class AcceptForDelivering(APIView):
    """
    Accept an order for delivery.
    """
    permission_classes = [IsAuthenticated, IsCourier]
    queryset = OrderModel

    def post(self, request):
        """
        Accept the order for delivery.
        """
        order = self.queryset.objects.filter(
            courier__id=request.user.pk).filter(order_status=OrderStatus.PENDING_COURIER)
        if order.exists():
            order = order.first()
            order.order_status = OrderModel.OrderStatus.DELIVERING
            order.save()
            return Response(data={
                "success": True,
                "message": "Order accepted for delivery",
                "data": order
            }, status=status.HTTP_200_OK)

        return Response(data={
            "success": False,
            "message": "No pending orders found for this courier"
        }, status=status.HTTP_400_BAD_REQUEST)


class MarkAsDelivered(APIView):
    """
    Mark an order as delivered.
    """
    permission_classes = [IsAuthenticated, IsCourier]
    queryset = OrderModel


    def post(self, request):
        """
        Mark the order as delivered.
        """
        order = self.queryset.objects.filter(
            courier__id=request.user.pk).filter(order_status=OrderModel.OrderStatus.DELIVERING)
        if order.exists():
            order = order.first()
            order.order_status = OrderModel.OrderStatus.DELIVERED
            order.save()
            return Response(data={
                "success": True,
                "message": "Order marked as delivered",
                "data": order
            }, status=status.HTTP_200_OK)

        return Response(data={
            "success": False,
            "message": "No pending delivery order found for this courier"
        }, status=status.HTTP_400_BAD_REQUEST)