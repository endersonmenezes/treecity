from django.db import models

# Create your models here.

class PrefeituraCadastro(models.Model):
    nome = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = '01 - Cadastros de Prefeituras'
        verbose_name = '01 - Cadastros de Prefeituras'

    def __str__(self):
        return str(self.nome)

class EmpresaCadastro(models.Model):
    nome = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = '02 - Cadastro de Empresas'
        verbose_name = '02 - Cadastro de Empresa'

    def __str__(self):
        return str(self.nome)
