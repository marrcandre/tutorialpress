from rest_framework import viewsets

from tutorialpress.core.models import Categoria, Publicacao
from tutorialpress.core.serializers import CategoriaSerializer, PublicacaoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
