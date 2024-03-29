from django.contrib import admin
from .models import *

# Register your models here.
models = [Department, Designation, Employee, Course, Video, Role, Assessment, Mark, AssessmentQuestion]

for model in models:
    admin.site.register(model)

