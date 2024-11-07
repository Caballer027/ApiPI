from django.db import models


class Usuario(models.Model):
    ESTUDIANTE = 'estudiante'
    PADRE = 'padre'
    APODERADO = 'apoderado'
    NORMAL = 'normal'
    
    TIPO_CUENTA_CHOICES = [
        (ESTUDIANTE, 'Estudiante'),
        (PADRE, 'Padre'),
        (APODERADO, 'Apoderado'),
        (NORMAL, 'Normal')
    ]

    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    tipo_cuenta = models.CharField(max_length=20, choices=TIPO_CUENTA_CHOICES)
    pfp = models.CharField(max_length=255, null=True, blank=True)  # Ruta de imagen de perfil
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class NivelAcademico(models.Model):
    id_nivel_academico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Grado(models.Model):
    id_grado = models.AutoField(primary_key=True)
    id_nivel_academico = models.ForeignKey(NivelAcademico, on_delete=models.CASCADE)
    nombre_grado = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_grado


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    id_grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Tema(models.Model):
    id_tema = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Dificultad(models.Model):
    FACIL = 'Facil'
    INTERMEDIO = 'Intermedio'
    DIFICIL = 'Dificil'
    
    NIVEL_CHOICES = [
        (FACIL, 'Fácil'),
        (INTERMEDIO, 'Intermedio'),
        (DIFICIL, 'Difícil')
    ]

    id_dificultad = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)

    def __str__(self):
        return self.nivel


class Leccion(models.Model):
    id_leccion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    id_nivel_dificultad = models.ForeignKey(Dificultad, on_delete=models.CASCADE)
    id_tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    puntos_obtenidos = models.DecimalField(max_digits=10, decimal_places=2)
    orden = models.IntegerField()

    def __str__(self):
        return self.titulo


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    enunciado = models.CharField(max_length=255)
    respuesta_correcta = models.CharField(max_length=255)
    id_leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.enunciado


class Intento(models.Model):
    id_intento = models.AutoField(primary_key=True)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_seleccionada = models.CharField(max_length=255)
    es_correcta = models.BooleanField()

    def __str__(self):
        return f"Intento {self.id_intento}"


class IntentoUsuario(models.Model):
    id_intento_usuario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_intento = models.ForeignKey(Intento, on_delete=models.CASCADE)

    def __str__(self):
        return f"IntentoUsuario {self.id_intento_usuario}"


class ProgresoUsuario(models.Model):
    id_progreso = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    completado = models.BooleanField()
    fecha_completado = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Progreso de {self.id_usuario} en {self.id_leccion}"


class RankingUsuario(models.Model):
    id_ranking = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntos_totales = models.IntegerField()
    posicion = models.IntegerField()

    def __str__(self):
        return f"Ranking {self.id_ranking}"


class PuntoUsuario(models.Model):
    id_punto = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    puntos_obtenidos = models.IntegerField()
    motivo = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Punto {self.id_punto} de {self.id_usuario}"


class UsuarioGrado(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_usuario', 'id_grado')

    def __str__(self):
        return f"Usuario {self.id_usuario} - Grado {self.id_grado}"
