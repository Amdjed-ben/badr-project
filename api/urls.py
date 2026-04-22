from django.urls import path
from . import views


urlpatterns = [
    path('client/add/', views.add_client, name='add client' ),
    path('projects/auth/', views.authenticate_project , name='authenticate project' ),
    path('projects/all/', views.list_projects, name='list-projects'),
    path('projects/list3/',views.list_3projects, name='list 3 projects'),
    path('categories/',views.list_category, name='list categories')

]
