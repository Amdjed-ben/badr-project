import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings') # استبدل اسم مشروعك هنا
django.setup()

from django.contrib.auth.models import User

username = 'amdjed'
email = 'amdjed.dev@proton.me'
password = '0662983272amd'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser {username} created successfully!")
else:
    print(f"Superuser {username} already exists.")