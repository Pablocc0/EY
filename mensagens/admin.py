from django.contrib import admin

# Register your models here.
from .models import Mensagem

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('texto', 'lido', 'criacao')