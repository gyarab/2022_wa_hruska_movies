from django.contrib import admin
from .models import Movie, Director

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'director', 'year', 'genres_display']
    list_display_links = ['name']
    search_fields = ['name']

admin.site.register(Movie)
admin.site.register(Director)
