from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/ledger_view.html"


class RecipeView(DetailView):
    model = Recipe
    template_name = "ledger/recipe_view.html"
