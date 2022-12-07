from blogs.views import * 
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'post-information',PostListCreateApiViewSet)



urlpatterns = [
    path('posts/',include(router.urls)),
    # path('post/<int:post_pk>/write_comment',comment_list,name='write-comment'),
    # path('comment/<int:pk>',comment_detail,name='comment-detail'),
    path('posts/<slug:category_slug>',CategoryApiView.as_view(),name='post_by_category'),
    path('search/<str:search_term>',SearchPostApiView.as_view(),name='search'),
]
