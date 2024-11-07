from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipesSearchForm, RecipeDataForm
from .utils import get_recipe_name, get_chart
from django.db.models import Q
import pandas as pd
from .forms import RecipeForm
from django.contrib import messages


# Create your views here.
@login_required
def home(request):
    return render(request, 'recipes/recipes_home.html')


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        # Start with all recipes
        queryset = Recipe.objects.all()
        form = RecipesSearchForm(self.request.GET or None)

        # If the form is submitted and valid, apply the filter
        if form.is_valid():
            search_term = form.cleaned_data.get('recipe_name')
            if search_term:
                # Filter by recipe name OR ingredients
                queryset = queryset.filter(
                    Q(name__icontains=search_term) | Q(ingredients__icontains=search_term)
                )
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipesSearchForm(self.request.GET or None)  # Keep the submitted form data
        return context

    def post(self, request, *args, **kwargs):
        # Handle the form for adding a recipe when the form is submitted via POST
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe added successfully!")
            return redirect('recipes:list')  # Redirect after successful submission
        else:
            messages.error(request, "Error adding recipe. Please check the form for errors.")
        
        # If the form is not valid, render the list view with the errors
        return self.get(request, *args, **kwargs)


# View for recipe lists, login required
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name= "recipes/recipe_details.html"

# View for recipe lists, login required
class RecipeDataView(LoginRequiredMixin, ListView):
    model = Recipe

    def get(self, request):
        form = RecipeDataForm()  # Use RecipeDataForm, which should contain `chart_type`
        recipes = Recipe.objects.all()
        return render(request, 'recipes/recipes_data.html', {'form': form, 'recipes': recipes})

    def post(self, request):
        form = RecipeDataForm(request.POST)  # Use RecipeDataForm in the post request
        chart = None  # Initialize chart to avoid potential NameError

        if form.is_valid():
            chart_type = form.cleaned_data.get('chart_type')  # Retrieve chart type from form
            recipe_name = form.cleaned_data.get('recipe_name')

            # Only filter if `recipe_name` has a value
            if recipe_name:
                qs = Recipe.objects.filter(Q(name__icontains=recipe_name) | Q(ingredients__icontains=recipe_name))
            else:
                qs = Recipe.objects.all()  # Retrieve all recipes if no `recipe_name` is provided

            if qs.exists():
                # Convert queryset to DataFrame and add difficulty column
                recipes = pd.DataFrame(qs.values())
                recipes['difficulty'] = recipes.apply(lambda row: get_recipe_name(row['id']).difficulty, axis=1)
                
                # Generate the chart based on chart_type
                chart = get_chart(chart_type, recipes, labels=recipes['id'].values)
            else:
                recipes = pd.DataFrame()  # Empty DataFrame if no recipes match

        context = {
            'form': form,
            'chart': chart,  # Pass chart to template
        }
        return render(request, 'recipes/recipes_data.html', context)
    

# Add Recipe view
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe added successfully!")
            return redirect('recipes:list')
        else:
            messages.error(request, "Error adding recipe. Please check the form for errors.")
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/add_recipe.html', {'form': form})


