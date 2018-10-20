from django.db import models

# Create your models here.

class BuscarAreas(models.Model):
    class Meta:
        verbose_name_plural = '01 - Árvores Patrocinadas'
        verbose_name = '01 - Árvores Patrocinadas'

    def __str__(self):
        return str(self.nome)

class CreditoC02(models.Model):
    class Meta:
        verbose_name_plural = '02 - Crédito de C02'
        verbose_name = '02 - Crédito de C02'

    def __str__(self):
        return str(self.nome)
