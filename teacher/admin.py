from django.contrib import admin

from teacher.models import Grade, Teacher

# Register your models here.
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'section', 'created_at']
    search_fields= ['name']
    list_filter = ['name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['name', 'phone' , 'age']    