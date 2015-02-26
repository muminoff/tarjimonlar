from haystack import indexes
from core.models import Member, Post, Comment


class MemberIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='name')

    def get_model(self):
        return Member

    def index_queryset(self, using=None):
        return Member.objects.all()


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='message')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return Post.objects.all()


class CommentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='message')

    def get_model(self):
        return Comment

    def index_queryset(self, using=None):
        return Comment.objects.all()
