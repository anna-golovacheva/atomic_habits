from rest_framework import permissions


class UserHabitPermissionManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user == view.get_object().user:
            return True
        return False
