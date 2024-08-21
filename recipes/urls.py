from django.urls import path
from .views import CategoryListCreate, RecipeListCreate, RecipeDetail, RecipeByCategoryName, RecipeByCategoryID

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    # path('recipes/category/<str:category_name>/', RecipeByCategoryName.as_view(), name='recipe-by-category-name'),
    path('recipes/category/<int:category_id>/', RecipeByCategoryID.as_view(), name='recipe-by-category-id'),
]
