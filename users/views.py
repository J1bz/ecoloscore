# -*- coding: utf-8 -*-

from rest_framework.authentication import (
    TokenAuthentication, SessionAuthentication)
from rest_framework.decorators import (
    authentication_classes, permission_classes)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

from django.contrib.auth.models import User
from users.permissions import (
    UpdateProfileIfOwnerOrReadOnly, UpdateUserIfSelfOrReadOnly)
from users.models import Profile
from users.serializers import ProfileSerializer, UserSerializer
from users.filters import UserFilter, ProfileFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((UpdateUserIfSelfOrReadOnly,))
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('username', 'email', 'first_name', 'last_name',)
    filter_class = UserFilter

    def update(self, request, pk=None):
        user = self.get_object()

        serializer = self.get_serializer(user, data=request.data)

        serializer.is_valid(raise_exception=True)

        if not request.user.is_staff:
            read_only_field_changed = False

            new_username = serializer.validated_data['username']
            new_is_staff = serializer.validated_data['is_staff']

            if new_username != user.username:
                read_only_field_changed = True

            if new_is_staff != user.is_staff:
                read_only_field_changed = True

            if read_only_field_changed:
                message = {'error': 'Only staff can update some fields'}
                return Response(message, status=HTTP_401_UNAUTHORIZED)

        serializer.save()
        return Response(serializer.data)


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((UpdateProfileIfOwnerOrReadOnly,))
class ProfileView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (FormParser, MultiPartParser,)
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('user__username', 'rfid_tag', 'favorite_song',)
    filter_class = ProfileFilter

    def update(self, request, pk=None):
        profile = self.get_object()

        serializer = self.get_serializer(profile, data=request.data)

        serializer.is_valid(raise_exception=True)

        if not request.user.is_staff:
            read_only_field_changed = False

            new_rfid_tag = serializer.validated_data['rfid_tag']
            new_user = serializer.validated_data['user']

            if new_rfid_tag != profile.rfid_tag:
                read_only_field_changed = True

            if new_user != profile.user:
                read_only_field_changed = True

            if read_only_field_changed:
                message = {'error': 'Only staff can update some fields'}
                return Response(message, status=HTTP_401_UNAUTHORIZED)

        serializer.save()
        return Response(serializer.data)
