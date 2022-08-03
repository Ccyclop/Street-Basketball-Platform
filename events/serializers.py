from rest_framework import serializers

from teams.serializers import TeamSerializer

from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'author', 'body', 'created_at']


class EventSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    participants = TeamSerializer(many=True, required=False)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'description', 'comments', 'happenes_at', 'participants']