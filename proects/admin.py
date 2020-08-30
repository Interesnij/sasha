from django.contrib import admin
from proects.models import Proect


class ProectAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title','slug','created']
    list_filter = ['created']
    class Meta:
        model = Proect

admin.site.register(Proect, ProectAdmin)
