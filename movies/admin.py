from django.contrib import admin
from movies.models import *


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'file', 'created']
    list_filter = ['created', 'category']
    search_fields = ['title', 'description', 'created']
    class Meta:
            model = Video

class VideoCommentAdmin(admin.ModelAdmin):
    list_display = ['text','commenter','created']
    list_filter = ['created']
    search_fields = ['created','text','commenter']
    class Meta:
            model = VideoComment

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoComment, VideoCommentAdmin)

admin.site.register(VideoFullscreen)
admin.site.register(VideoBanner)
