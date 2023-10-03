from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=40)
    caga_horaria = models.IntegerField()
    data_criação = models.DateTimeField()
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        """Melhorando a saida"""
        return self.nome