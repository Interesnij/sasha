from django.contrib import admin
from movies.models import Video, VideoComment


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created']
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
