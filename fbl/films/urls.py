from django.urls import path
from django.conf.urls.static import static

from fbl import settings
from .views import *
from django.urls import path, include
from django.conf.urls.static import static

from films.views import *

urlpatterns = [
    path(
        "", MainPage.as_view(), name="home"
    ),  
    path("films/<slug:gen_slug>", FilmGenreView.as_view(), name="f_genre"),
    path("serials/<slug:gen_slug>", SerialGenreView.as_view(), name="s_genre"),
    path("multfilmi/all", MultiGenreView.as_view(), name="mult_genre")
    
]


    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
