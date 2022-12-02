from django.db import IntegrityError
from django.contrib.auth.models import User
from dotenv import load_dotenv
import os

load_dotenv()

try:
    superuser = User.objects.create_superuser(
        username=os.getenv('SUPER_USER_NAME'),
        email=os.getenv('SUPER_USER_EMAIL'),
        password=os.getenv('SUPER_USER_PASSWORD')
    )
    superuser.save()
except IntegrityError:
    print(f"Super User with username '{os.getenv('SUPER_USER_NAME')}' already exists!")
except Exception as e:
    print(e)
