from rest_framework import permissions


# Custom permission class to allow owners to modify their own objects
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow safe methods (GET, HEAD, OPTIONS) for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the owner of the object matches the requesting user
        return obj.owner == request.user
