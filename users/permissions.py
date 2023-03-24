from rest_framework import permissions


class UserRetrievePermissionManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user == view.get_object():
            return True
        return False
