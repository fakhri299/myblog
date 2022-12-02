from django.shortcuts import render
from blogs.serializer import PostSerializer,CommentSerializer,CategorySerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView,CreateAPIView,ListAPIView
from blogs.models import Post,Comment,Category
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.query_utils import Q


# Create your views here.
class PostListCreateApiView(ListCreateAPIView):
    serializer_class=PostSerializer
    queryset=Post.objects.all()



class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    lookup_url_kwarg='kitab_pk'


class CommentListCreateApiView(ListCreateAPIView):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()

    def perform_create(self, serializer,**kwargs):
        post_pk=self.kwargs.get('kitab_pk')
        post=Post.objects.get(pk=post_pk)
        serializer.save(post=post)


class CommentDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()
    lookup_url_kwarg='comment_pk'



class CategoryListApiView(ListAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()



class CategoryApiView(APIView):
    def get(self,request,category_slug):
        post_by_category=Post.objects.filter(category__slug=category_slug)
        serializer=PostSerializer(post_by_category,many=True)
        return Response({'Uygun postlar':serializer.data})




class SearchPostApiView(APIView):
    def get(self,request,search_term):
        matches = Post.objects.filter(
        Q(title__icontains=search_term) |
        Q(category__name__icontains=search_term) |
        Q(description__icontains=search_term))
        
        if matches is not None:
           serializer = PostSerializer(matches, many=True)
           return Response({'Neticeler':serializer.data})
                     

        else:
           return Response('not')       

        

           
       

        
    
     
