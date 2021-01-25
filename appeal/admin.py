from django.contrib import admin
from appeal.models import *


class AnswerInline(admin.TabularInline):
    model = Answer

class SurveyAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_anonymous', 'is_multiple', 'is_no_edited', 'time_end']
    inlines = [
        AnswerInline,
    ]
    search_fields = ('title',)


admin.site.register(Survey, SurveyAdmin)
admin.site.register(SurveyVote)

admin.site.register(Appeal)
