from django.contrib import admin
from .models import appointment
from .models import applyToGrad
from .models import Classes
from .models import Grades

admin.site.register(appointment)
admin.site.register(applyToGrad)
admin.site.register(Classes)
admin.site.register(Grades)
