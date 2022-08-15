from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ForeignKey(
        'self', 
        null= True,
        blank= True,
        on_delete= models.DO_NOTHING,
        related_name='following')


class post(models.Model):
    content = models.CharField(max_length=280)
    time = models.DateTimeField()
    user = models.ForeignKey(
        User, 
        on_delete= models.SET('Deleted user'),
        related_name= 'posts'
        )
    likes = models.ManyToManyField(
        User,
        blank=True, 
        null= True,
        related_name='allLikedUser',
        )
    
    def __str__(self) -> str:
        return f'{self.time}: {self.user}: {self.likes}'
