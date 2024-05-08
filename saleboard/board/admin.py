from django.contrib import admin

from board.models import Bd, Rubric


class BdAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bd, BdAdmin)
admin.site.register(Rubric)
