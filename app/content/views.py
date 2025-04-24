from .models import Post, Reel
from .serializers import PostSerializer, ReelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes.add(request.user)
        post.dislikes.remove(request.user)
        return Response({'status': 'liked'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def dislike(self, request, pk=None):
        post = self.get_object()
        post.dislikes.add(request.user)
        post.likes.remove(request.user)
        return Response({'status': 'disliked'})


class ReelViewSet(viewsets.ModelViewSet):
    queryset = Reel.objects.all().order_by('-created_at')
    serializer_class = ReelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def like(self, request, pk=None):
        reel = self.get_object()
        reel.likes.add(request.user)
        return Response({'status': 'liked'})
