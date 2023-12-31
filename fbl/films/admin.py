from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "time_create",
        "poster",
        "is_publish",
        "actors",
        "poster",
        "rate",
        "video",
        "typ"
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    # список полей, редактируемых с админки
    list_editable = ["is_publish"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Movie, MovieAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Genre, GenreAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(MenuItem, MenuAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(MovieType, TypeAdmin)