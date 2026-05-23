from django.contrib import admin

from movie.models import Category, Movie

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields =['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','release_date','language']
    autocomplete_fields = ['category']