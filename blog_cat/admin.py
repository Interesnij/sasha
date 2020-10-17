from django.contrib import admin
from blog_cat.models import BlogCategory


class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_filter = ['name']
    search_fields = ('name',)
    class Meta:
        model = BlogCategory

admin.site.register(BlogCategory, BlogCategoryAdmin)
