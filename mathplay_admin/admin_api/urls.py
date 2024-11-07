from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet,
    NivelAcademicoViewSet,
    GradoViewSet,
    CursoViewSet,
    TemaViewSet,
    LeccionViewSet,
    PreguntaViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'niveles-academicos', NivelAcademicoViewSet)
router.register(r'grados', GradoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'temas', TemaViewSet)
router.register(r'lecciones', LeccionViewSet)
router.register(r'preguntas', PreguntaViewSet)

urlpatterns = router.urls
