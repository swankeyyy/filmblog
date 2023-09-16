from django.urls import path

from .views import *

urlpatterns = [
    path(
        "", MainPage.as_view(), name="home"
    ),  # нужно вызывать функцию чтобы класс заработал
    
]
