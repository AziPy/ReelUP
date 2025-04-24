from rest_framework import serializers
from .models import Post, Reel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'likes', 'dislikes')


class ReelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reel
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'likes')
