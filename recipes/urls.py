from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, RecipeDataView

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path("list/", RecipeListView.as_view(), name="list"),
    path("list/<int:pk>/", RecipeDetailView.as_view(), name="detail"),
    path('data/', RecipeDataView.as_view(), name='data'),
]
