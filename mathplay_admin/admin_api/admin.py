from django.contrib import admin
from .models import (
    Usuario,
    NivelAcademico,
    Grado,
    Curso,
    Tema,
    Dificultad,
    Leccion,
    Pregunta,
    Intento,
    IntentoUsuario,
    ProgresoUsuario,
    RankingUsuario,
    PuntoUsuario,
    UsuarioGrado
)

# Registrar todos los modelos en el panel de administración de Django
admin.site.register(Usuario)
admin.site.register(NivelAcademico)
admin.site.register(Grado)
admin.site.register(Curso)
admin.site.register(Tema)
admin.site.register(Dificultad)
admin.site.register(Leccion)
admin.site.register(Pregunta)
admin.site.register(Intento)
admin.site.register(IntentoUsuario)
admin.site.register(ProgresoUsuario)
admin.site.register(RankingUsuario)
admin.site.register(PuntoUsuario)
admin.site.register(UsuarioGrado)
