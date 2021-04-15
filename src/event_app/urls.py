from django.urls import path, include
from .views import PostListView, PostCreateView, PostRemoveSerializer, PostEditSerializer

urlpatterns = [
    path('api/posts/', PostListView.as_view()),
    path('api/posts/create/', PostCreateView.as_view()),
    path('api/posts/remove/', PostRemoveSerializer.as_view()),
    path('api/posts/edit/', PostEditSerializer.as_view()),
]
