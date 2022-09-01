from rest_framework import permissions


class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to read only or edit for admin or owners of an object.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff) or (obj.user == request.user)


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to read only or edit for admin.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
