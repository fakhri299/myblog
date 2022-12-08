from blogs.serializer import PostSerializer,CommentSerializer,CategorySerializer
from rest_framework.generics import ListAPIView
from blogs.models import Post,Comment,Category
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.query_utils import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from blogs.permissions import OwnProfilorReadOnly,OwnCommentorReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView,CreateAPIView


# Create your views here.
class PostListCreateApiViewSet(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.newmanager.all()
    permission_classes=[OwnProfilorReadOnly,IsAuthenticatedOrReadOnly]



class CommentCreateApiView(CreateAPIView):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()

    def perform_create(self, serializer,**kwargs):
        post_pk=self.kwargs.get('post_pk')
        post=Post.objects.get(pk=post_pk)
        author=self.request.user
        serializer.save(post=post,author=author)


class CommentDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()
    permission_classes=[IsAuthenticated,OwnCommentorReadOnly]



class CommentListApiView(ListAPIView):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()



class CategoryApiView(APIView):
    def get(self,request,category_slug):
        post_by_category=Post.objects.filter(category__slug=category_slug)
        serializer=PostSerializer(post_by_category,many=True)
        return Response({'Related posts':serializer.data})




class SearchPostApiView(APIView):
    def get(self,request,search_term):
        matches = Post.objects.filter(
        Q(title__icontains=search_term) |
        Q(category__name__icontains=search_term) |
        Q(description__icontains=search_term))
        
        if matches is not None:
           serializer = PostSerializer(matches, many=True)
           return Response({'Results':serializer.data})
                     

        else:
           return Response('not')       

        

           
       

        
    
     
