from django.shortcuts import render
from users.models import User

from rest_framework import generics, permissions, serializers
from rest_framework.mixins import UpdateModelMixin

from .permissions import TeamActionsPermissions, IsPlayer
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer, PlayerCreationSerializer, TeamCreateSerializer, PlayerUpdateSerializer
from mixins import RequestMethodSerializerClassMixin
 

class TeamListView(RequestMethodSerializerClassMixin, generics.ListCreateAPIView):
    queryset = Team.objects.all()
    method_serializer_classes = {
        ('GET',): TeamSerializer,
        ('POST',): TeamCreateSerializer,
    }
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeamDetailView(RequestMethodSerializerClassMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    method_serializer_classes = {
        ('GET',):TeamSerializer,
        ('PUT',): TeamCreateSerializer,
        ('DESTROY',): TeamCreateSerializer,
        ('PATCH',): TeamCreateSerializer,
    }
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TeamActionsPermissions]


class TeamMembersView(RequestMethodSerializerClassMixin, generics.ListCreateAPIView):
    
    method_serializer_classes = {
        ('GET',): PlayerSerializer,
        ('POST',): PlayerCreationSerializer,
    }

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        queryset = Player.objects.filter(team=Team.objects.get(pk=self.kwargs['pk']))
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request=request, *args, **kwargs)
    

class PlayerDetailView(RequestMethodSerializerClassMixin, generics.RetrieveUpdateDestroyAPIView):

    queryset = Player.objects.all()

    method_serializer_classes = {
        ('GET',): PlayerSerializer,
        ('PUT',): PlayerUpdateSerializer,
        ('PATCH',): PlayerUpdateSerializer,
        ('DESTROY',): PlayerUpdateSerializer
    }  

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsPlayer]
    
    
    



