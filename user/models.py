from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, verbose_name='학번')
    password = models.TextField()
    name = models.CharField(max_length=100, verbose_name='이름')
    email = models.deletion()
    permission = models.IntegerField(default=0)
