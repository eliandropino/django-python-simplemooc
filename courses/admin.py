from django.contrib import admin

# Register your models here.
from .models import Course

#course admin customiza a listagem no painel dos cursos
class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Course, CourseAdmin)