from django.contrib import admin
from .models import Students
from .models import Classes
from .models import Grades

admin.site.register(Students)
admin.site.register(Classes)
admin.site.register(Grades)
