from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blogs.models import Post,Category,Comment


class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class PostSerializer(ModelSerializer):
    category=CategorySerializer(read_only=True)
    class Meta:
        model=Post
        fields='__all__'


class CommentSerializer(ModelSerializer):
    post=PostSerializer(read_only=True)
    class Meta:
        model=Comment
        fields='__all__'
        

