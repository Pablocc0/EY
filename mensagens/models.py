from django.db import models


# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Mensagem(Base):
    texto = models.CharField(max_length=255)
    lido = models.BooleanField(True)
    
    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

        def __str__(self):
            return self.texto
