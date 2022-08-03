from django.shortcuts import render

from rest_framework import generics, permissions, serializers

from mixins import RequestMethodSerializerClassMixin

from .permissions import UserActionsPermissions
from .models import User
from teams.serializers import UserSerializer
from .serializers import UserUpdateSerializer

class ProfileView(RequestMethodSerializerClassMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    method_serializer_classes = {
        ('GET',): UserSerializer,
        ('PUT',): UserUpdateSerializer,
        ('PATCH',): UserUpdateSerializer,
        ('DELETE',): UserUpdateSerializer
    }

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserActionsPermissions]
