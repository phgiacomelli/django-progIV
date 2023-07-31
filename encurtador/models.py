from django.db import models
from .utils import gerador_codigo


# Create your models here.
class URL(models.Model):
    # cria campo url, do tipo CharField, tamanho máximo 220:
    url = models.CharField(max_length=220)

    # cria campo shortcode, tamanho máximo 15
    shortcode = models.CharField(max_length=15, unique=True, blank=True)

    # campos autopreenchidos p/ data de atualização e criação
    atualizado = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print("save foi executado")
        # testa se o shortcode é nulo ou está em branco
        if self.shortcode is None or self.shortcode == "":
            # mesmo que: if self.shortcode in (None,""):
            self.shortcode = gerador_codigo()
        # chama o método save() da classe super (pai):
        super(URL, self).save(*args, **kwargs)

    # método que retorna string com identificação do objeto
    def __str__(self):
        # return str(self.pk)  # retorna a chave primária
        return str(self.url)  # retorna a propriedade url
