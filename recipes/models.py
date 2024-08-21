from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.JSONField()  # Use JSONField for a list of ingredients
    instructions = models.TextField()  # Use TextField for instructions
    category_id = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
