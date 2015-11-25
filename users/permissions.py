# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateUserIfSelfOrReadOnly(BasePermission):
    """
    Allow users to change their informations and others to read
    """

    def has_object_permission(self, request, view, user):
        if request.method in SAFE_METHODS:
            return True

        if request.method in ['PUT', 'PATCH']:
            return request.user == user or request.user.is_staff

        return False


class UpdateProfileIfOwnerOrReadOnly(BasePermission):
    """
    Allow users whose profile belong to to edit it (but not create other
    profiles nor destroy it) and the rest of the world to read.
    """

    def has_object_permission(self, request, view, profile):
        if request.method in SAFE_METHODS:
            return True

        if request.method in ['PUT', 'PATCH']:
            return request.user == profile.user or request.user.is_staff

        return False
