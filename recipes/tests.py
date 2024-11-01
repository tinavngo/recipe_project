from django.test import TestCase, Client
from .models import Recipe
from django.urls import reverse
from .utils import get_chart, get_recipe_name
import pandas as pd
from django.contrib.auth.models import User
from .views import home

# Create your tests here.
class RecipeModelTest(TestCase):

    def setUpTestData():
        # set up recipe object for testing
        Recipe.objects.create(name='Tea', ingredients='Sugar, Water, Tea Leaves', cooking_time=3)

    def test_recipe_name(self):
        # fetch recipe object by id
        recipe = Recipe.objects.get(id=1)
        # get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('name').verbose_name
        # compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_ingredient_max_length(self):
        # fetch recipe object by id
        recipe = Recipe.objects.get(id=1)
        # get the metadata for the 'ingredients' field and use it to query its data
        max_length = recipe._meta.get_field('ingredients').max_length
        # compare the value to the expected result
        self.assertEqual(max_length, 200)

    def test_cooking_time_integer(self):
        # fetch recipe object by id
        recipe = Recipe.objects.get(id=1)
        # checks if the object is an integer
        self.assertIsInstance(recipe.cooking_time, int)
        # checks if the object is greater than 0
        self.assertGreater(recipe.cooking_time, 0)


class RecipeViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')
        self.recipe = Recipe.objects.create(name="Test Recipe", ingredients="ingredient1, ingredient2", cooking_time=20)

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipes:detail', kwargs={'pk': self.recipe.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')

    def test_recipe_detail_view_with_nonexistent_recipe(self):
        response = self.client.get(reverse('recipes:detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)

class RecipeDataViewTests(TestCase):
    
    def setUp(self):
        # Set up test data
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')
        Recipe.objects.create(name="Test Recipe 1", ingredients="ingredient1, ingredient2", cooking_time=20)
        Recipe.objects.create(name="Test Recipe 2", ingredients="ingredient3, ingredient4", cooking_time=30)
        
    def test_recipe_data_view_get(self):
        response = self.client.get(reverse('recipes:data'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Collection Data')

    def test_recipe_data_view_post_valid(self):
        response = self.client.post(reverse('recipes:data'), {
            'chart_type': '1',
            'recipe_name': 'Test Recipe 1'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'img')

    def test_get_recipe_name(self):
        recipe = Recipe.objects.get(name="Test Recipe 1")
        self.assertEqual(get_recipe_name(recipe.id), recipe)
