from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read allowed for any request - GET, HEAD, OPTIONS always allowed

        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission only allowed to the owner of the snippet.
        # Checked after making sure that we don't just want to read.
        return obj.owner == request.user
