from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsRecipientOrReadOnly(permissions.BasePermission):
    """
    Custom permission class to allow read-only access for all users
    and deletion only for the recommendation recipient.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.recommended_to == request.user
