from django.shortcuts import redirect, render
from blog.forms import CategoryForm, PostForm
from blog.models import Category, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.functions import Lower


def home(request):
    return render(request, 'blog/home.html')

# function to logout user
def logout_user(request):
    logout(request)
    return render(request,'blog/logout.html')

# function to login user
def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            messages.error(request, 'Credenciais Inválidas')
    return render(request,'blog/login.html')

# function to register user
def register_user(request):
    if (request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username,None, password)
        except:
            #catch
            return render(request,'blog/error.html')
        else:
            return render(request,'blog/success.html')
    return render(request, 'blog/register.html')

#function to list all recipes with search functionality
def list_recipes(request):
    recipes = Post.objects.all()
    categories = Category.objects.all()
    if request.method == 'GET':
        recipes = Post.objects.all()
        categories = Category.objects.all()
    elif request.method == 'POST':
        field = request.POST.get('field', '').strip().lower()
        recipes = Post.objects.filter(title__icontains=field) | Post.objects.filter(category__category__icontains=field) | Post.objects.filter(ingredients__icontains=field) | Post.objects.filter(recipe__icontains=field)
    return render(request, 'blog/list_recipes.html', {'recipes':recipes, 'categories':categories, 'recipes_all':recipes})


# function to add a new post with optional category creation
@login_required(login_url='blog:login_user')
# with this, @login_required decorator, only authenticated users can access this view.
def add_post(request):
    form_category = CategoryForm()
    form_post = PostForm()
    if request.method == 'POST':
        form_post = PostForm(request.POST, request.FILES)
        if form_post.is_valid():
                new_category = request.POST['new_category']
                if new_category:
                    # add new category to the database if it doesn't exist already
                    category, created = Category.objects.get_or_create(category=new_category)
                    # update the post
                    form_post.instance.category = category
                form_post.save()
                return redirect('blog:list_recipes')
    return render(request, 'blog/add_post.html', {
        'form_post': form_post, 
        'form_category': form_category,
    })

# function to show details of a recipe
def details_post(request, id):
    recipes_all = Post.objects.all()
    categories = Category.objects.all()
    recipe = Post.objects.get(pk=id)
    form_post = PostForm(instance=recipe)
    return render(request, 'blog/details_post.html', {'form_post':form_post, 'recipe':recipe, 'categories':categories, 'recipes_all': recipes_all})

# function to edit a recipe
@login_required(login_url='blog:login_user')
def edit_post(request, id):
    recipe = Post.objects.get(pk=id)
    form_post = PostForm(instance=recipe)
    if request.method == 'POST':
        form_post = PostForm(request.POST, request.FILES, instance=recipe)
        form_post.save()
        return redirect('blog:list_recipes')
    return render(request, 'blog/edit_post.html', {'form_post':form_post, 'recipe':recipe})

# function to delete
@login_required(login_url='blog:login_user')
def delete_post(request, id):
    recipe = Post.objects.filter(pk=id)
    recipe.delete()
    return redirect("blog:list_recipes")

# function to filter by category
def filter_by_category(request, id):
    if request.method == 'GET':
        categories = Category.objects.all().order_by(Lower('category')) # get all categories to show in details_post.html
        recipes = Post.objects.filter(category_id=id)
        recipes_all = Post.objects.all()
    return render(request, 'blog/list_recipes.html', {'categories':categories, 'recipes':recipes, 'recipes_all':recipes_all})

# function to show all recipes in alphabetical order
def index_a_z(request, id):
    recipes_all = Post.objects.all().order_by(Lower('title'))
    categories = Category.objects.all()
    recipe = Post.objects.get(pk=id)
    form_post = PostForm(instance=recipe)
    return render(request, 'blog/details_post.html', {'form_post':form_post, 'recipe':recipe, 'categories':categories, 'recipes_all': recipes_all})
