from django.contrib import admin
from djangoApp1.models import Tutor, Basic_User_Model

# Super Users:
# 1. 
# username: alvin
# password: alvinadler
# email: alvin@gmail.com

# Register your models here.
admin.site.register(Tutor)
admin.site.register(Basic_User_Model)
