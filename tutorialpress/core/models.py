from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)


class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    is_publicada = models.BooleanField(default=False)
