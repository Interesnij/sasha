from django.contrib import admin
from forms.models import Blank


class BlankAdmin(admin.ModelAdmin):
    search_fields = ('title')
    list_display = ['title','file']
    list_filter = ['created']
    class Meta:
        model = Blank

admin.site.register(Blank, BlankAdmin)
