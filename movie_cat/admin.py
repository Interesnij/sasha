from django.contrib import admin
from movie_cat.models import VideoCategory


class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','order']
    list_filter = ['name']
    search_fields = ('name',)
    class Meta:
        model = VideoCategory

admin.site.register(VideoCategory, VideoCategoryAdmin)
