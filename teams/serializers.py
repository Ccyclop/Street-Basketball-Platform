from rest_framework import serializers
from users.models import User

from .models import Team, Player 


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar']


class PlayerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'player', 'position']


class PlayerCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'player', 'team', 'position']


class PlayerSerializer(serializers.ModelSerializer):
    player = UserSerializer(many=False)

    class Meta:
        model = Player
        fields = ['id', 'player', 'team', 'position']


class TeamSerializer(serializers.ModelSerializer):
    members = PlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']


class TeamCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name']

