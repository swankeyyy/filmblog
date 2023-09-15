from django.contrib import admin
from .models import *

#Импортируем все модели, чтобы они были доступны в админке и регистрируем
#Создаем класс и прописываем поля таблицы в админке конкретно к этой модели

class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'poster', 'is_publish', 'actors', 'poster', 'rate', 'video')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    #список полей, редактируемых с админки
    list_editable = ['is_publish']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Film, FilmAdmin)
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name', )}
    
admin.site.register(Genre, GenreAdmin)