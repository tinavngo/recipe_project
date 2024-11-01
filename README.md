# RecipMe

This web-based Recipe Application, developed with Python and Django, enables users to search for recipes by ingredients, automatically assigns a difficulty rating to each recipe, and allows users to contribute their own creations. The application includes user authentication, an administrative dashboard with Django, and offers data analysis features on recipe data.

## Live Demo
Hosted on Heroku: https://ghostly-fangs-31914-5bddee25b209.herokuapp.com/

## Getting started

1. Clone the repository: git clone https://github.com/yourusername/recipe_project.git    cd recipe-project
2. Create a virtual environment: python3 -m venv venv source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies: Install all the required modules listed in requirements.txt: pip install -r requirements.txt
4. Set up the database: python manage.py migrate
5. Create a superuser for Django Admin: python manage.py createsuperuser
6. Run the development server: python manage.py runserver
7. Access the app: http://127.0.0.1:8000/
8. Access Django Admin to manage database entries through the admin dashboard, log in at http://127.0.0.1:8000/admin/
  ```


## Requirements
- Python 3.13 and Django 5 are required.
- Handles exceptions and displays user-friendly error messages for invalid input
- During development, the app uses an SQLite database, while in production, it connects to a locally-hosted PostgreSQL database.
- The app has an easy-to-use interface with clear instructions and forms.
- Code is properly documented, with automated tests included.
- A requirements.txt file lists all necessary modules for the project.
- Instructions for downloading and running the app locally are provided below.


## Contribution
* [Tina Ngo](https://github.com/tinavngo/recipe_project)

## License
This project is licensed under the MIT License.