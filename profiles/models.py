from django.db import models

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    email = models.CharField()
    job = models.CharField()
    age = models.IntegerField()
    bio = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
