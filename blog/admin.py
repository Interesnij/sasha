from django.contrib import admin
from blog.models import Blog, BlogComment


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created']
    list_filter = ['created', 'category']
    search_fields = ['title', 'description', 'created']
    exclude = ('creator', 'count')

    class Meta:
            model = Blog

    def get_changeform_initial_data(self, request):
        return {'creator': request.user}

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['text','commenter','created']
    list_filter = ['created']
    search_fields = ['created','text','commenter']

    class Meta:
            model = BlogComment

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
