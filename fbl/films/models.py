from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название фильма")
    content = models.TextField(blank=True, verbose_name="Описание")
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True, verbose_name="URL"
    )
    time_create = models.DateField(auto_now_add=True)
    is_publish = models.BooleanField(default=True)
    actors = models.TextField(blank=True, verbose_name="В главных ролях")
    create_date = models.DateField(verbose_name="Дата выхода")
    poster = models.ImageField(upload_to="posters/", verbose_name="Постер")
    rate = models.TextField(max_length=1, verbose_name="Рейтинг Кинопоиска")
    video = models.URLField(verbose_name="Ссылка на трейлер")
    opinion = models.TextField(blank=True, verbose_name="Отзыв")
    genre = models.ManyToManyField("Genre", verbose_name="Жанры", blank=True)
    typ = models.ForeignKey("MovieType", verbose_name="Тип", on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        
        return reverse("film", kwargs={"movie_slug": self.slug})

    class Meta:
        verbose_name = "Список фильмов"
        ordering = ["time_create", "title"]

    def __str__(self):
        return f"self.title"

class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def __str__(self) -> str:
        return self.name

    def get_film_url(self):
        return reverse("f_genre", kwargs={"gen_slug": self.slug})
    
    def get_serial_url(self):
        return reverse("s_genre", kwargs={"gen_slug": self.slug})
    
    def get_multi_url(self):
        return reverse("mult_genre", kwargs={"all": "all"})

    class Meta:
        verbose_name = "Жанры"
        
class MenuItem(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Пункт меню")
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name="URL")
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("menu", kwargs={"item_slug": self.slug})

    class Meta:
        verbose_name = "Пункты меню"
        
        
class MovieType(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Тип")
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name="URL")
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("film_type", kwargs={"type_slug": self.slug})

    class Meta:
        verbose_name = "Тип"