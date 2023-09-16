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
# from .forms import *
from .models import *
# from .utils import DataMixin

class MainPage(ListView):
    model = Film
    template_name = 'films/index.html'
    context_object_name = "film_list"
    
    def get_context_data(
        self, **kwargs
    ):  # задает дополнительные параметры которые передаются в шаблон
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Главная страница"
        return context

    def get_queryset(self):
        return Film.objects.all()[::-1]

