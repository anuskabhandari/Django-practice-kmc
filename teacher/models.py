from django.db import models

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length= 20 , help_text="Enter grade name", verbose_name="Grade Name")
    section = models.CharField(max_length= 5 , default="A")
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    def __str__(self):
        return f'{self.name} - {self.section}'

    class Meta:  # To overwrite sth we use meta otherwise the table name will be displayed as app-name_table-name
        db_table = "grade"
        unique_together = ['name', 'section'] # both name should be different not same

class Teacher(models.Model):
    grade = models.ForeignKey(Grade,on_delete=models.SET_NULL, related_name="grade_teacher", null=True)
    name = models.CharField(max_length=60, help_text="teacher name")
    phone = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "teacher"
