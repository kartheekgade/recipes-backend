from rest_framework import generics
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        # Check if the data is a list
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            return Response({'error': 'Data must be a list of objects.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate and save the data
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        # Check if the data is a list
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            return Response({'error': 'Data must be a list of objects.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate and save the data
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
class RecipeByCategoryName(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        try:
            category = Category.objects.get(name=category_name)
            return Recipe.objects.filter(category=category)
        except Category.DoesNotExist:
            return Recipe.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"detail": "Category not found or no recipes available."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class RecipeByCategoryID(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Recipe.objects.filter(category_id=category_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"detail": "No recipes found for this category ID."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)