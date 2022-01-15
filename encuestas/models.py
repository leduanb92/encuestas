from django.db import models


# Create your models here.
class InteresPersonal(models.Model):
    value = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Intereses Personales'

    def __str__(self):
        return self.value


class Encuesta(models.Model):
    MASCULINO = 'm'
    FEMENINO = 'f'
    SEX_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]
    GRADOS_ESCOLARIDAD_CHOICES = [
        ('p', 'Primaria'),
        ('s', 'Secundaria'),
        ('tm', 'Técnico Medio'),
        ('pre', 'Preuniversitario'),
        ('ns', 'Nivel Superior'),
    ]

    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEX_CHOICES)
    grado_de_escolaridad = models.CharField(max_length=3, choices=GRADOS_ESCOLARIDAD_CHOICES)
    peso_corporal = models.FloatField(verbose_name='Peso corporal (Kg)')
    intereses_personales = models.ManyToManyField(InteresPersonal)


    def __str__(self):
        return 'Encuesta realizada por %s' % self.nombre

