from rest_framework import serializers
from .models import Post,PostImage


class PostListSerializer(serializers.ModelSerializer):
    images = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        exclude = ('description','phone','category')


class PostCreateSerializer(serializers.ModelSerializer):
    # images = serializers.CharField(read_only=True)

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    class Meta:
        model = Post
        exclude = ('id',)


class PostRemoveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"


class PostEditSerializer(serializers.ModelSerializer):

    def edit(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Post
        exclude = ('id',)
