from django.shortcuts import render

from rest_framework import generics, permissions

from .permissions import IsAuthorOrReadOnly, IsEventAuthorForCommentDeletion
from .models import Post, Comment
from .serializers import EventSerializer, CommentSerializer

class EventsView(generics.ListCreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Post.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class EventCreateComment(generics.ListCreateAPIView):

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.filter(post=Post.objects.get(pk=self.kwargs['pk']))
        return queryset

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(author=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))

class EventComments(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly, IsEventAuthorForCommentDeletion]