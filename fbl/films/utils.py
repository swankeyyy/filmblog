from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["menu_genres"] = Genre.objects.all()
        context["menu"] = MenuItem.objects.all()
        return context
