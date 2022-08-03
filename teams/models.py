from django.db import models

from users.models import User

class Team(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

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
    
    