from django.db import models
from django.conf import settings
from hashids import Hashids


class Member(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True)
    name = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.name)

    @property
    def posts_count(self):
        return Post.objects.filter(creator=self).count()

    def get_posts(self):
        return Post.objects.filter(creator=self)

    @property
    def comments_count(self):
        return Comment.objects.filter(creator=self).count()

    def get_comments(self):
        return Comment.objects.filter(creator=self)

    def get_hashid(self):
        hashids = Hashids(salt='tarjimonlar')
        return hashids.encode(int(self.id))

    def get_texts_from_posts_and_comments(self):
        posts = [''.join(p.message) for p in Post.objects.filter(creator=self)]
        comments = [''.join(c.message) for c in Comment.objects.filter(creator=self)]
        return posts + comments


    class Meta:
        db_table = 'members'


class Post(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    message = models.TextField()
    created_time = models.DateTimeField(db_index=True)
    updated_time = models.DateTimeField()
    creator = models.ForeignKey(Member, db_index=True)
    likes = models.IntegerField(db_index=True)

    def __unicode__(self):
        return self.id
    def get_comments(self):
        return Comment.objects.filter(post=self)

    def get_comments_count(self):
        return Comment.objects.filter(post=self).count()

    def get_type(self):
        return 'post'

    def get_hashid(self):
        hashids = Hashids(salt='tarjimonlar')
        return hashids.encode(int(self.id.split('_')[1]))

    class Meta:
        db_table = 'posts'
        ordering = ['-created_time', '-updated_time']


class Comment(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True)
    message = models.TextField()
    created_time = models.DateTimeField(db_index=True)
    creator = models.ForeignKey(Member, db_index=True)
    post = models.ForeignKey(Post, db_index=True)
    likes = models.IntegerField(db_index=True)

    def __unicode__(self):
        return self.id

    def get_type(self):
        return 'comment'

    class Meta:
        db_table = 'comments'
        ordering = ['-created_time']
