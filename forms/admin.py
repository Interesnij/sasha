from django.contrib import admin
from forms.models import Blank


class BlankAdmin(admin.ModelAdmin):
    list_display = ['title','file','order']
    list_filter = ['created']
    search_fields = ('title',)
    class Meta:
        model = Blank

admin.site.register(Blank, BlankAdmin)
