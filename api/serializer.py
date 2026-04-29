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
    # def get_image(self, obj):
    #     if obj.image:
    #         return obj.image.url
    #     return None
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if instance.image:
    #         # هذا السطر يضمن تحويل المسار النسبي إلى رابط كامل
    #         representation['image'] = self.context['request'].build_absolute_uri(instance.image.url)
    #     return representation
class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Categore
        fields = "__all__"
