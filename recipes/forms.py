from django import forms

CHART__CHOICES = (
   ('1', 'Pie chart'),
   ('2', 'Bar chart'),
   ('3', 'Line Chart'),
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=100)

class RecipeDataForm(forms.Form):
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)