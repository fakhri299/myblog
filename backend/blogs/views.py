from blogs.serializer import PostSerializer,CommentSerializer,CategorySerializer
from rest_framework.generics import ListAPIView
from blogs.models import Post,Comment,Category
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models.query_utils import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from blogs.permissions import OwnProfilorReadOnly,OwnCommentorReadOnly,IsAdminUserOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView,CreateAPIView
from blogs.filters import PostFilter,CategoryFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class PostListCreateApiViewSet(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.newmanager.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    permission_classes=[OwnProfilorReadOnly,IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer,**kwargs):
        author=self.request.user
        serializer.save(author=author)
   



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



class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    permission_classes = [IsAdminUserOrReadOnly]







class SearchPostApiView(APIView):
    def get(self,request,search_term):
        matches = Post.objects.filter(
        Q(title__icontains=search_term) |
        Q(category__name__icontains=search_term) |
        Q(description__icontains=search_term)|
        Q(author__username=search_term))
        
        if matches:
           serializer = PostSerializer(matches, many=True)
           return Response({'Results':serializer.data})
                     

        else:
           return Response('Not matches')       

        

           
       

        
    
     
