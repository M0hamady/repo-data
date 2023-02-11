from  rest_framework import permissions
from rest_framework.permissions import BasePermission

from useres.models import User


class IsManagerUser(BasePermission):
    """
    Allows access only to manager users.
    """

    def has_permission(self, request, view):
        return bool(request.user and User.objects.get(user=request.user.id).is_manager)

class IsEngUser(BasePermission):
    """
    Allows access only to is_eng users.
    """

    def has_permission(self, request, view):
        return bool(request.user and User.objects.get(user=request.user).is_eng)

class IsDesignerUser(BasePermission):
    """
    Allows access only to is_designer users.
    """

    def has_permission(self, request, view):
        return bool(request.user and User.objects.get(user=request.user).is_designer)

class IsAccountantUser(BasePermission):
    """
    Allows access only to accountant users.
    """

    def has_permission(self, request, view):
        return bool(request.user and User.objects.get(user=request.user).is_accountant)

