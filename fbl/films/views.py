from django.shortcuts import render
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet
from django.http import *
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import *
from django.urls import reverse_lazy


from .models import *
from .utils import DataMixin


class MainPage(DataMixin, ListView):
    model = Movie
    template_name = "films/index.html"
    context_object_name = "film_list"

    def get_context_data(
        self, **kwargs
    ):  # задает дополнительные параметры которые передаются в шаблон
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(page_title="Главная страница")
        context = dict(list(context.items()) + list(mix_context.items()))
        return context

    def get_queryset(self):
        return Movie.objects.all()[::-1]


class FilmGenreView(DataMixin, ListView):
    model = Movie
    template_name = "films/genres.html"
    context_object_name = "genres_list"
    allow_empty = False

    def get_context_data(
        self, **kwargs
    ):  # задает дополнительные параметры которые передаются в шаблон
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(page_title="Фильмы по жанрам")
        context = dict(list(context.items()) + list(mix_context.items()))
        return context

    def get_queryset(self):
        return Movie.objects.filter(
            genre__slug=self.kwargs["gen_slug"], is_publish=True, typ__slug="film"
        )[::-1]


class SerialGenreView(DataMixin, ListView):
    model = Genre
    template_name = "films/genres.html"
    context_object_name = "genres_list"
    allow_empty = False

    def get_context_data(
        self, **kwargs
    ):  # задает дополнительные параметры которые передаются в шаблон
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(page_title="Сериалы по жанрам")
        context = dict(list(context.items()) + list(mix_context.items()))
        return context

    def get_queryset(self):
        return Movie.objects.filter(
            genre__slug=self.kwargs["gen_slug"], is_publish=True, typ__slug="serial"
        )[::-1]


class MultiGenreView(DataMixin, ListView):
    model = Genre
    template_name = "films/genres.html"
    context_object_name = "genres_list"
    allow_empty = False

    def get_context_data(
        self, **kwargs
    ):  # задает дополнительные параметры которые передаются в шаблон
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(page_title="Мультфильмы")
        context = dict(list(context.items()) + list(mix_context.items()))
        return context

    def get_queryset(self):
        return Movie.objects.filter(
            is_publish=True,
            typ__slug="multfilm",
        )[::-1]


class ShowPost(DataMixin, DetailView):
    model = Movie
    template_name = "films/post.html"
    context_object_name = "post"
    slug_url_kwarg = "movie_slug"

    def get_context_data(
        self, **kwargs
    ):  # задает дополнительные параметры которые передаются в шаблон
        context = super().get_context_data(**kwargs)
        
        mix_context = self.get_user_context(page_title=context["post"].title)
        context = dict(list(context.items()) + list(mix_context.items()))
        return context
        

    
