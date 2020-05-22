from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)


class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    is_publicada = models.BooleanField(default=False)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        related_name="publicacoes",
        related_query_name="publicacao",
        null=True,
        blank=True,
    )
