from django.urls import path

from .views import ledger_view, recipe1_view, recipe2_view

urlpatterns = [
    path('recipes/list', ledger_view, name='Recipe Book'),
    path('recipe/1', recipe1_view, name='Recipe 1'),
    path('recipe/2', recipe2_view, name='Recipe 2')
]

app_name = 'ledger'
