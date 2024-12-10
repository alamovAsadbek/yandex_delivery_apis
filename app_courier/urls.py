from django.urls import path

from app_courier import views


urlpatterns = [
    path('my-deliveries/', views.MyDeliveredDeliveries.as_view(), name='my_deliveries'),
    path('accept-for-delivery/', views.AcceptForDelivering.as_view(), name='accept_for_delivery'),
    path('mark-as-delivered/', views.MarkAsDelivered.as_view(), name='mark_as_delivered'),
]