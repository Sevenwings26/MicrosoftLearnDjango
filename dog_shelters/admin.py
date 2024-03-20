from django.contrib import admin
# from . import models
from .models import Shelter, Dog

# # Login details 
# username: admin_ll
# password: admin123

# Register your models here.
admin.site.register(Shelter)
admin.site.register(Dog) 
