from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length= 100 , null = True , blank = True , help_text="teacher full name", verbose_name="Teacher Name")
    subject = models.CharField(max_length= 100)
    contact_number = models.PositiveIntegerField(default= 0)
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return f'{self.teacher_name}'

    class Meta:  # To overwrite sth we use meta otherwise the table name will be displayed as app-name_table-name
        db_table = "teacher"