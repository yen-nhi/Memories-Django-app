from django.db import models
from django.db.models.base import Model

class Profile(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='profile_user')
    uid = models.CharField(max_length=35)
    avatar = models.CharField(max_length=500)


class Memory(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='memory_user')
    name = models.CharField(max_length=150)
    comment = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    def serialize(self):
        return {
            'username': self.user.username,
            'name': self.name,
            'comment': self.comment,
            'location': self.location,
        }