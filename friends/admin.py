from django.contrib import admin
from friends.models import Friend


class FriendAdmin(admin.ModelAdmin):
    list_display = ['link', 'image',]
    search_fields = ('link',)
    class Meta:
        model = Friend

admin.site.register(Friend, FriendAdmin)
