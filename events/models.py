from django.db import models

from users.models import User
from teams.models import Team

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Team, blank=True)

    title = models.CharField(max_length=255)
    description = models.TextField()
    likes = models.IntegerField(default=0)

    happenes_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    body = models.TextField()
    likes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title
    
    
