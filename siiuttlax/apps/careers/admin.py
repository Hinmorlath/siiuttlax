from django.contrib import admin
from .models import Career


@admin.register(Career)
class careersAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'level', 'name')
    ordering = ['level', 'short_name']


#@admin.register(Subject)
#class SubjectAdmin(admin.ModelAdmin):
    #list_display=['name', 'career', 'semester', 'sema']
    #list_filter = ['carrer', 'semester']