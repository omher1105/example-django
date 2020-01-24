from django.contrib import admin

# Register your models here.
from persona.models import PersonaModel


@admin.register(PersonaModel)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'direccion',)
    list_filter = ('nombre',)
    sortable_by = ('nombre', 'direccion',)
