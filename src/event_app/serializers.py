from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')


class PostCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        links = validated_data.pop('links')
        post = Post(**validated_data)
        post.save()
        if links:
            for i in links:
                post.links.add(i)
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
