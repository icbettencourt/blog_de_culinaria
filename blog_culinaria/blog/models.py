from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Post(models.Model):
    # title of the recipe
    title = models.CharField(max_length=200)
    # photo of the recipe
    photo = models.ImageField(upload_to="blog/", blank=True, null=True)
    # ingredients of the recipe
    ingredients = models.TextField(blank=True, null=True)
    # description of the recipe
    recipe = models.TextField(blank=True, null=True)
    # category of the recipe
    category = models.ForeignKey(Category, on_delete=models.PROTECT,  blank=True, null=True)
    # created date of the recipe
    created_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.category}"