from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blogs.models import Post,Category,Comment
from django.contrib.auth.models import User


class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class PostSerializer(ModelSerializer):
    category=serializers.StringRelatedField(read_only=True)
    author=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'


class CommentSerializer(ModelSerializer):
    author=serializers.StringRelatedField()
    post=PostSerializer(read_only=True)
    class Meta:
        model=Comment
        fields='__all__'
        

