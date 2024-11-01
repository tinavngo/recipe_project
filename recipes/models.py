from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length= 120)
    ingredients = models.CharField(max_length= 200, help_text="Enter the ingredient, separated by comma")
    cooking_time = models.PositiveIntegerField( help_text='Enter time in minutes')
    difficulty = models.CharField(max_length=20, blank= True)
    description = models.TextField(default='There is no description for this recipe.')
    pic= models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        # Reverse function returns and absolute path matching a given view and optional parameters.
        return reverse ('recipes:detail', kwargs={'pk': self.pk})
    
    def return_ingredients_as_list(self):
        return self.ingredients.split(",")
    
    def calculate_difficulty(self):
        ingredients = self.ingredients.split(',')
        if self.cooking_time < 30:
            return 'Easy' if len(ingredients) < 6 else 'Medium'
        else:
            return 'Intermediate' if len(ingredients) < 6 else 'Hard'
        
    def save(self, *args, **kwargs):
        self.difficulty = self.calculate_difficulty()
        super().save(*args, **kwargs)
