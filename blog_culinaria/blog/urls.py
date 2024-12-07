from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('user/logout', views.logout_user, name='logout_user'),
    path('user/login', views.login_user, name='login_user'),
    path('user/register', views.register_user, name='register_user'),
    path('add_post', views.add_post, name='add_post'),
    path('list_recipes', views.list_recipes, name='list_recipes'),
    path('details_post/<int:id>', views.details_post, name='details_post'),
    path('edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('filter_by_category/<int:id>', views.filter_by_category, name='filter_by_category'),
    path('index_a_z/<int:id>', views.index_a_z, name='index_a_z'),
]

