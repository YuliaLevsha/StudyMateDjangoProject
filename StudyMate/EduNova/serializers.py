from rest_framework import serializers
from .models import *


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['uuid', 'name', 'percent', 'uuid_user']


class ArticleSerializer(serializers.ModelSerializer):
    uuid_topic = TopicSerializer(required=True)

    class Meta:
        model = Article
        fields = ['uuid', 'text', 'header', 'uuid_topic', 'next_article', 'head']

