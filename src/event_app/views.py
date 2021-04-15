from django.shortcuts import render
from .models import Post
from .serializers import PostListSerializer, PostCreateSerializer, PostRemoveSerializer, PostEditSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer


class PostRemoveSerializer(DestroyAPIView):
    serializer_class = PostRemoveSerializer


class PostEditSerializer(UpdateAPIView):
    serializer_class = PostEditSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'
    queryset = Post.objects.all()