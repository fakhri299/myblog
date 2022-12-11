from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blogs.models import Post,Comment,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class PostSerializer(ModelSerializer):
    author=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Post
        fields='__all__'



        


class CommentSerializer(ModelSerializer):

    author=serializers.StringRelatedField()
    post=PostSerializer(read_only=True)
   
    class Meta:
        model=Comment
        fields='__all__'


    
    