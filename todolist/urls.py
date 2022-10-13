from django.urls import path
from todolist.views import show_todolist
from todolist.views import login_user, register, logout_user, create_task
from todolist.views import show_json, add_todolist_item

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'),
    path('add/', add_todolist_item, name='add_todolist_item'),
]