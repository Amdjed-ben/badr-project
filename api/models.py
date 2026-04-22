from django.db import models
from django.contrib.auth.hashers import make_password, identify_hasher

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField( max_length=254, default="")
    number = models.CharField(max_length=254,default="00")
    facebook_link = models.CharField(max_length=254,default="",null=True,blank=True)
    
    description = models.TextField(max_length=1500,default="") 
    def __str__(self):
        return self.name

class Categore(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(default="",null=True,blank=True)
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=254,default='')
    description = models.TextField(max_length=2000, default='')
    link = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=254)
    image = models.ImageField(upload_to='project_pics/',blank=True,null=True)
    categore = models.ForeignKey(Categore, on_delete= models.PROTECT,blank=True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # التأكد من أن كلمة المرور ليست مشفرة بالفعل قبل تشفيرها
        # (حتى لا نقوم بتشفير الـ Hash مرة أخرى عند كل عملية تعديل)
        try:
            identify_hasher(self.password)
        except ValueError:
            # إذا لم تكن مشفرة، قم بتشفيرها الآن
            self.password = make_password(self.password)
            
        super().save(*args, **kwargs)