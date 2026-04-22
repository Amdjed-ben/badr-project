from django.contrib import admin
from .models import Clients,Project,Categore
from django import forms
from django.utils.html import format_html

# Register your models here.

admin.site.site_header = "Badr Project Management"
admin.site.site_title = "Badr Admin Portal"
admin.site.index_title = "Welcome to your Dashboard"
admin.site.enable_nav_sidebar = True

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            # هنا نضع الـ widget لتظهر النجوم
            'password': forms.PasswordInput(render_value=True),
        }

@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display =('name', 'email', 'number')
    search_fields = ('name', 'email', 'number')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    list_display = ('title', 'created_at', 'categore') # الأعمدة التي تظهر في القائمة
    search_fields = ('title', 'description')

    fields = ('title', 'description', 'link', 'password',"categore", 'image', 'display_image')
    readonly_fields = ('display_image',)

    # widgets = {
    #         # تحويل حقل النص إلى حقل نجوم في الواجهة
    #         'password': forms.PasswordInput(render_value=True),
    #     }
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:150px; height: auto;border-raduis: 20px;border: 3px solid black" />',obj.image.url)
        return 'no value'
    display_image.short_discription = 'see pic'
    # def display_password_stars(self, obj):
    #     return "********"
    
    # display_password_stars.short_description = "Password"

@admin.register(Categore)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')