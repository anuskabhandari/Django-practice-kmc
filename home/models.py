from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length= 100 , null = True , blank = True , help_text="student full name", verbose_name="Student Name")
    dob = models.DateField()
    contact_number = models.PositiveIntegerField(default= 0)
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return f'{self.name}'

    class Meta:  # To overwrite sth we use meta otherwise the table name will be displayed as app-name_table-name
        db_table = "student"

class StudentProfile(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    student_card_no= models.PositiveIntegerField(unique=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.student_id}'

    class Meta:
        db_table = "student_profile"
