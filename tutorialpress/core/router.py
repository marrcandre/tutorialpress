from rest_framework import routers

from tutorialpress.core.views import CategoriaViewSet, PublicacaoViewSet

router = routers.SimpleRouter()
router.register("categorias", CategoriaViewSet)
router.register("publicacoes", PublicacaoViewSet)
