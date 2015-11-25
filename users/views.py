# -*- coding: utf-8 -*-

from rest_framework.authentication import (
    TokenAuthentication, SessionAuthentication)
from rest_framework.decorators import (
    authentication_classes, permission_classes)
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter

from django.contrib.auth.models import User
from common.permissions import IsAdminOrAuthentReadOnly
from users.models import Profile
from users.serializers import ProfileSerializer, UserSerializer
from users.filters import UserFilter, ProfileFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('username', 'email', 'first_name', 'last_name',)
    filter_class = UserFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class ProfileView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('user__username', 'rfid_tag', 'favorite_song',)
    filter_class = ProfileFilter
