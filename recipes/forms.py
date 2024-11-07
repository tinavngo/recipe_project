from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHART__CHOICES = (
   ('1', 'Pie chart'),
   ('2', 'Bar chart'),
   ('3', 'Line Chart'),
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=100)

class RecipeDataForm(forms.Form):
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

