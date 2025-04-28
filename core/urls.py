from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/content/', include('app.content.urls')),
    path('api/users/', include('app.users.urls')),  # 💥 Добавлено
] + urls_swagger

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
