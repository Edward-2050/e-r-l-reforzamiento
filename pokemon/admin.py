from django.contrib import admin
from .models import Pokemon


# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    fields =  ('nombre', 'numero', 'tipo')
    search_fields = ('nombre',)
    list_display = ('nombre', 'generacion', 'tipo')
