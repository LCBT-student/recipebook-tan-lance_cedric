from django.urls import path

from .views import RecipeView, RecipeListView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipes-list'),
    path('recipe/<int:pk>', RecipeView.as_view(), name='recipe_view')
]

app_name = 'ledger'
