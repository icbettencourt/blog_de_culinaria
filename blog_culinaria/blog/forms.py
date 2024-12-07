from datetime import date
from django import forms
from blog.models import Category, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Título ...'}),
            'ingredients': forms.Textarea(attrs={'placeholder':'Ingredientes ...'}),
            'recipe': forms.Textarea(attrs={'placeholder':'Preparação ...'}),
            'created_date': forms.DateInput(attrs={'type':'date'}),
        }

