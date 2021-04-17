from django.urls import path, include
from .views import PostListView, PostCreateView, PostRemoveView, PostEditSerializer

urlpatterns = [
    path('api/posts/', PostListView.as_view()),
    path('api/posts/create/', PostCreateView.as_view()),
    path('api/posts/remove/<int:post_id>/', PostRemoveView.as_view()),
    path('api/posts/edit/', PostEditSerializer.as_view()),
]
