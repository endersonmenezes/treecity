from django.contrib import admin
from .models import CadastrarArea, CadastrarMuda, NovaQuest, AbatimentoIPTU

# Register your models here.

admin.site.register(CadastrarMuda)
admin.site.register(CadastrarArea)
admin.site.register(NovaQuest)
admin.site.register(AbatimentoIPTU)
