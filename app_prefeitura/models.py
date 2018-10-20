from django.db import models

# Create your models here.

class CadastrarArea(models.Model):
    class Meta:
        verbose_name_plural = '01 - Nova Região da Cidade'
        verbose_name = '01 - Nova Região da Cidade'

    def __str__(self):
        return str(self.nome)

class CadastrarMuda(models.Model):
    class Meta:
        verbose_name_plural = '02 - Cadastrar Muda para Adoção'
        verbose_name = '02 - Cadastrar Muda para Adoção'

    def __str__(self):
        return str(self.nome)

class NovaQuest(models.Model):
    class Meta:
        verbose_name_plural = '03 - Nova Quest para População'
        verbose_name = '03 - Nova Quest para População'

    def __str__(self):
        return str(self.nome)

class AbatimentoIPTU(models.Model):
    class Meta:
        verbose_name_plural = '04 - Consultar Cashback IPTU'
        verbose_name = '04 - Consultar Cashback IPTU'

    def __str__(self):
        return str(self.nome)