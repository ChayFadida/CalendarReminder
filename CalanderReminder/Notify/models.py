from django.db import models
# Create your models here.


class UsersFriends(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, auto_created=True)
    full_name = models.CharField(max_length=200)
    birthday = models.DateField()
    special_occasions = models.CharField(blank=True, max_length=1000)
    remind_before = models.BooleanField(default=False)