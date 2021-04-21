from django.shortcuts import render
from .models import Post
from .serializers import PostListSerializer, PostCreateSerializer, PostRemoveSerializer, PostEditSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class PostCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostCreateSerializer


class PostRemoveView(DestroyAPIView):
    serializer_class = PostRemoveSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'
    queryset = Post.objects.all()


class PostEditSerializer(UpdateAPIView):
    serializer_class = PostEditSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'
    queryset = Post.objects.all()