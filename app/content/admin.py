from django.contrib import admin
from .models import Reel, Post


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
