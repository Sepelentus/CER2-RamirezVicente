from django.contrib import admin

# Register your models here.
from .models import Conserje, Correspondencia, Residencia

admin.site.register(Residencia)
admin.site.register(Conserje)
admin.site.register(Correspondencia)