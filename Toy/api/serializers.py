from rest_framework import serializers
from .models import Article, Writer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'status',
                  'created_at', 'written_by', 'edited_by',)


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ('is_editor', 'user')


class HomeSerializers(serializers.Serializer):
    user_name = serializers.CharField(max_length=200)
    user_id = serializers.IntegerField()
    article_count = serializers.IntegerField()
    last_30_days_count = serializers.IntegerField()


class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content')    