from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MyProfileView, UserProfileView, LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', MyProfileView.as_view(), name='my-profile'),
    path('profile/<int:user__id>/', UserProfileView.as_view(), name='user-profile'),
]
