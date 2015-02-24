from django.db import models


class Member(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.name)

    @property
    def get_comments_count(self):
        return Comment.objects.filter(creator=self).count()

    class Meta:
        db_table = 'members'


class Post(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    message = models.TextField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    creator = models.ForeignKey(Member)
    likes = models.IntegerField()

    def __unicode__(self):
        return self.id

    def get_comments(self):
        return Comment.objects.filter(post=self)

    def get_comments_count(self):
        return Comment.objects.filter(post=self).count()

    class Meta:
        db_table = 'posts'
        ordering = ['-created_time', '-updated_time']


class Comment(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    message = models.TextField()
    created_time = models.DateTimeField()
    creator = models.ForeignKey(Member)
    post = models.ForeignKey(Post)
    likes = models.IntegerField()

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'comments'
        ordering = ['-created_time']