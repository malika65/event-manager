from django.shortcuts import render
from .models import Post
from .serializers import PostListSerializer,PostCreateSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView

class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer

