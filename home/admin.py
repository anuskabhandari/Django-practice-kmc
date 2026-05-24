from django.contrib import admin

from home.models import Student, StudentProfile 

# Register your models here.
#admin.site.register(Student)

## admin panel ma user wala table ma search field , ani list ma dekhine and filter xaa but hamile banayeko student table ma xaina soo for making that
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'contact_number']
    search_fields= ['name']
    list_filter = ['is_active', 'name']

@admin.register(StudentProfile)
class StudetProfileAdmin(admin.ModelAdmin):
    list_display = ['student','address','email']    