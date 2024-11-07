from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe


CHART__CHOICES = (
   ('1', 'Pie chart'),
   ('2', 'Bar chart'),
   ('3', 'Line Chart'),
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=100)

class RecipeDataForm(forms.Form):
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'cooking_time', 'difficulty', 'description', 'pic']
        
    # Optional: Add help_text or custom widgets
    # For example, for the ingredients field
    ingredients = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter ingredients, separated by commas.'}),
        help_text="Enter ingredients separated by commas."
    )
    # Optionally add custom validation or cleaning logic
    def clean_ingredients(self):
        ingredients = self.cleaned_data.get('ingredients')
        if not ingredients:
            raise forms.ValidationError("Please provide at least one ingredient.")
        return ingredients