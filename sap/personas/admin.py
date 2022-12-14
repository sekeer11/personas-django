from django.contrib import admin

# Register your models here.
from personas.models import Persona, Domicilio

admin.site.register(Persona)
admin.site.register(Domicilio)