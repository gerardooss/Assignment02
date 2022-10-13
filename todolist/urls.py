# TODO: Implement Routings Here
from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_ajax, name='show_ajax'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_activity, name='add_activity'),
    path('delete/<int:id>', delete, name='delete'),
    path('status/<int:id>', status, name='status'),
    path('json/', show_json, name='show_json'),
]