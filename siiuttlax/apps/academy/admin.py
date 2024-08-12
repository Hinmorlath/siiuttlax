from django.contrib import admin
from .models import Professor, Student, Category

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'category', 'employee_number', 'title')
    fields = ('first_name', 'last_name', 'category', 'employee_number', 'title','email')

@admin.register(Student)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrollment')
    fields = ('first_name', 'last_name', 'enrollment','email')

admin.site.register(Category)