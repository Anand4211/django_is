from django.contrib import admin
from blogs.models import Poost

# Register your models here.
class PoostAdmin(admin.ModelAdmin):
    list_display=['slug','title','author','body','publish','create','updated','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('author','status')
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
admin.site.register(Poost,PoostAdmin)


