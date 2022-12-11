from blogs.views import * 
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'',PostListCreateApiViewSet)



urlpatterns = [
    path('posts/',include(router.urls)),
    path('posts/<int:post_pk>/write_comment',CommentCreateApiView.as_view(),name='write-comment'),
    path('comments/<int:pk>',CommentDetailApiView.as_view(),name='comment-detail'),
    path('comments/',CommentListApiView.as_view(),name='comment-list'),
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('search/<str:search_term>',SearchPostApiView.as_view(),name='search'),
]
