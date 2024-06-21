from django.contrib import admin
from .models import Professor, Student, Principal

admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Principal)