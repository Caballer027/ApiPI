from rest_framework import viewsets
from .models import Usuario, NivelAcademico, Grado, Curso, Tema, Leccion, Pregunta
from .serializers import (
    UsuarioSerializer,
    NivelAcademicoSerializer,
    GradoSerializer,
    CursoSerializer,
    TemaSerializer,
    LeccionSerializer,
    PreguntaSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class NivelAcademicoViewSet(viewsets.ModelViewSet):
    queryset = NivelAcademico.objects.all()
    serializer_class = NivelAcademicoSerializer

class GradoViewSet(viewsets.ModelViewSet):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
