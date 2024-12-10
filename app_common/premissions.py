from rest_framework.permissions import BasePermission, SAFE_METHODS

from app_users.models import UserRoleChoice


class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.status == UserRoleChoice.ADMIN


class IsRestaurant(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoleChoice.RESTAURANT


class IsBranch(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoleChoice.DELIVERY


class IsCourier(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoleChoice.COURIER


class IsUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or request.user.is_authenticated and request.user == obj


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or request.user.is_authenticated and request.user == obj.user