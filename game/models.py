from django.db import models

#A model for active games to be displayed
class activeGame(models.Model):
    gameName = models.CharField(max_length=200)
    gameDesc = models.CharField(max_length=200)
    masterName = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.gameName
