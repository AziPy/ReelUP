from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ReelViewSet, LoadMorePostsView, LoadMoreReelsView

# Инициализируем роутер
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'reels', ReelViewSet)

urlpatterns = [
    # Подключаем стандартные ViewSet маршруты
    path('', include(router.urls)),

    # Добавляем кастомные маршруты для пагинации
    path('load-more-posts/', LoadMorePostsView.as_view(), name='load_more_posts'),
    path('load-more-reels/', LoadMoreReelsView.as_view(), name='load_more_reels'),
]
