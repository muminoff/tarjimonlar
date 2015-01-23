from django.db import models


class GroupUser(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=100)

