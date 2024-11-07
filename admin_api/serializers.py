from rest_framework import serializers
from .models import Usuario, NivelAcademico, Grado, Curso, Tema, Leccion, Pregunta

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class NivelAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelAcademico
        fields = '__all__'

class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'

class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'
