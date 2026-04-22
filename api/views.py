from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view # pyright: ignore[reportMissingImports]
from rest_framework.response import Response # pyright: ignore[reportMissingImports]
from rest_framework import status  # pyright: ignore[reportMissingImports]
from .serializer import Clients_Serializer,Project_Serializer,Category_Serializer
from .models import Clients,Project,Categore
from django.contrib.auth.hashers import check_password
# Create your views here.
@api_view(["POST"])
def add_client(req):
    serializer = Clients_Serializer(data = req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def authenticate_project(req):
    p_id = req.data.get('id')
    p_password = req.data.get('password')

    if not p_id or not p_password:
        return Response({"error":"please send the id and the password"})
    
    try:
        project_instance = Project.objects.get(id = p_id)

        if check_password(p_password,project_instance.password):
            return Response({
                "status": "success",
                "message": "Password correct",
                "project_title": project_instance.title,
                "project_link": project_instance.link
            }, status=status.HTTP_200_OK)
        else:
            return Response({"status": "failed", "message": "Wrong password try again"}, status=status.HTTP_401_UNAUTHORIZED)
    
    except Project.DoesNotExist:
        return Response({"error": "the project does not exist"},status=status.HTTP_404_NOT_FOUND)
    
@api_view(["GET"])
def list_projects(req):
    list = Project.objects.all()
    serializer = Project_Serializer(list,context = {'request':req}, many=True)
    
    return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(["GET"])
def list_3projects(req):
    projects = Project.objects.all().order_by('-id')[:3]
    serializer = Project_Serializer(projects,context = {'request':req}, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def list_category(req):
    categories = Categore.objects.all()
    serializer = Category_Serializer(categories, context={'request':req},many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
