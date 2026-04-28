from django.urls import path,re_path
from . import views


urlpatterns = [
    path('client/add/', views.add_client, name='add client' ),
    path('projects/auth/', views.authenticate_project , name='authenticate project' ),
    path('projects/all/', views.list_projects, name='list-projects'),
    path('projects/list3/',views.list_3projects, name='list 3 projects'),
    path('categories/',views.list_category, name='list categories')
]
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import re

# أضف هذا بعد urlpatterns الحالية
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]