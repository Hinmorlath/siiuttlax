from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import careers

@admin.register(careers)
class careersAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'short_name', 'status', 'director')
    search_fields = ('name', 'short_name', 'director')
    list_filter = ('level', 'status')
