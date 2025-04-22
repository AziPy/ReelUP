from django.contrib import admin
from .models import Book, BookGenre, BookTag, Reel, Post
from .models.book import BookComment


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(BookTag)
class BookTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at')
    search_fields = ('title', 'user__email')
    list_filter = ('created_at',)
    filter_horizontal = ('genre', 'tags')


@admin.register(Reel)
class ReelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'video_preview')
    search_fields = ('user__email',)
    list_filter = ('created_at',)
    filter_horizontal = ('likes',)

    def video_preview(self, obj):
        return f"🎥 Video ID {obj.id}" if obj.video else "No video"

    video_preview.short_description = "Video"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'image_preview')
    search_fields = ('user__email',)
    list_filter = ('created_at',)
    filter_horizontal = ('likes',)

    def image_preview(self, obj):
        return f"📷 Image ID {obj.id}" if obj.image else "No image"

    image_preview.short_description = "Image"


@admin.register(BookComment)
class BookCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'created_at', 'text', 'parent']
    search_fields = ['user__username', 'book__title', 'text']
    list_filter = ['book', 'parent']  # Фильтрация по родительскому комментарию
    list_display_links = ['user', 'book']  # Указываем кликабельные поля
