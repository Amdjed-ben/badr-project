from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Clients,Project,Categore

class Clients_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"

class Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id",'title','description',"categore",'password','image']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        def get_photo_url(self,obj):
            req = self.context.get('request')
            photo_url = obj.fingerprint.url
            return req.build_absolute_url()
class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Categore
        fields = "__all__"
