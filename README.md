Backend: Django

The backend is developed using Django, providing API endpoints for the frontend to fetch data. The application uses Django REST Framework to handle HTTP requests and responses.
API Endpoints:
/categories/: Retrieves a list of all recipe categories.
/recipes/category/{category_id}/: Fetches recipes based on the selected category.
/recipes/{recipe_id}/: Fetches the recipe details based on the selected recipe.

Data Flow:
Category List: When the user selects a category, the frontend sends a request to the ‘/categories/’ endpoint to retrieve the list of available categories.
Recipe List: Upon selecting a category, the frontend triggers an API call to `/recipes/category/{category_id}/`, fetching and displaying relevant recipes.
Recipe Details: Upon selecting a recipe, the frontend triggers an API call to `/recipes/{recipe_id}/`

Technologies Used:
Django for the backend framework.
Django REST Framework for creating API endpoints.
SQLite for the database.
