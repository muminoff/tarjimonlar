from haystack import indexes
from core.models import Member, Post, Comment


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='message')

    created_time = indexes.DateTimeField(model_attr='created_time')
    updated_time = models.DateTimeField(model_attr='updated_time')
    likes = indexes.IntegerField(model_attr='likes')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return Post.objects.all()


class CommentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='message')
    created_time = indexes.DateTimeField(model_attr='created_time')
    likes = indexes.IntegerField(model_attr='indexes')

    def get_model(self):
        return Comment

    def index_queryset(self, using=None):
        return Comment.objects.all()
