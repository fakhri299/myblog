from blogs.views import * 
from django.urls import path

urlpatterns = [
    path('posts/',PostListCreateApiView.as_view(),name='post-list'),
    path('post/<int:kitab_pk>',PostDetailApiView.as_view(),name='post-detail'),
    path('post/<int:kitab_pk>/write_comment',CommentListCreateApiView.as_view(),name='write-comment'),
    path('comment/<int:pk>',CommentDetailApiView.as_view(),name='comment-detail'),
    path('posts/<slug:category_slug>',CategoryApiView.as_view(),name='post_by_category'),
]
