#!/bin/python

import sys
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ops.settings")

import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()

def get_users():
    for user in User.objects.all():
        print(user.username)

if __name__ == "__main__":
    get_users()
