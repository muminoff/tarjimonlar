from django.db import models


class GroupUser(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()
    # email = models.EmailField()


# class Post(models.Model):
#     id = models.CharField(primary_key=True)
#     created_time = models.DateTimeField()
#     updated_time = models.DateTimeField()
#     from_name = models.ForeignKey(GroupUser)



# class Comment(models.Model):
#     pass
