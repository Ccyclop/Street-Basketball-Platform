from rest_framework import serializers
from users.models import User

from .models import Team, Player, Feedback


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
    owner = UserSerializer(many=False)
    members = PlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'owner', 'name', 'members', 'location', 'challanged']


class TeamCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Team
        fields = ['id', 'owner', 'name', 'location']


class FeedbackSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_at = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Feedback
        fields = ['id', 'author', 'body', 'stars', 'created_at']