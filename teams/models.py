from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import User

class Team(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=False, default='None')
    challanged = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Player(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='members')

    POSITION_CHOICES = (
        ('C', 'Captain'),
        ('P', 'Player'),
        ('B', 'Bench')
    )

    position = models.CharField(choices=POSITION_CHOICES, max_length=100, default='Player')

    def __str__(self):
        return self.player.username
    
    
class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    body = models.TextField()
    stars = models.IntegerField(default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.team.name} - {self.author.username}'