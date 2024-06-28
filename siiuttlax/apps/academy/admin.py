from django.contrib import admin
from .models import Professor, Student, Category

admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Category)