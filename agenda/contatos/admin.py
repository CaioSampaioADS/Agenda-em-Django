from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email', 'mostrar')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

