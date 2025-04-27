from .models import Post, Reel
from .serializers import PostSerializer, ReelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework import status
from django.core.paginator import Paginator

class LoadMorePostsView(APIView):
    def get(self, request):
        page_number = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('size', 10))

        all_items = Post.objects.all()  # Получаем все посты
        paginator = Paginator(all_items, page_size)

        try:
            page = paginator.page(page_number)
        except:
            return Response({'error': 'Invalid page.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PostSerializer(page.object_list, many=True)

        response = {
            'items': serializer.data,
            'has_next': page.has_next(),
            'has_previous': page.has_previous(),
            'num_pages': paginator.num_pages,
            'current_page': page.number,
        }

        return Response(response)


class LoadMoreReelsView(APIView):
    def get(self, request):
        page_number = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('size', 10))

        all_items = Reel.objects.all()  # Получаем все рилсы
        paginator = Paginator(all_items, page_size)

        try:
            page = paginator.page(page_number)
        except:
            return Response({'error': 'Invalid page.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReelSerializer(page.object_list, many=True)

        response = {
            'items': serializer.data,
            'has_next': page.has_next(),
            'has_previous': page.has_previous(),
            'num_pages': paginator.num_pages,
            'current_page': page.number,
        }

        return Response(response)


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
