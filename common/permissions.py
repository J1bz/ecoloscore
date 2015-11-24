# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrAuthentReadOnly(BasePermission):
    """
    Custom permission to only allow admins to edit objects and authenticated
    users to read it.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated()

        return request.user and request.user.is_staff
