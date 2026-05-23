from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=150)
    category = models.ManyToManyField(Category)
    release_date = models.DateField()
    language = models.CharField(max_length=10,null=True, blank=True)


    def __str__(self):
        return self.name