# -*- coding: utf-8 -*-
from locale import *
import csv,sys,os

project_dir = '../sasha/sasha/'

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django, json, requests

django.setup()
from users.models import User

User.objects.all().delete()
