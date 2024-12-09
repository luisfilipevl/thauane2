from django.db import models
from usuarios.models import UserBlog

class Voo(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    data_publicacao = models.DateField(auto_created=True)
    texto = models.TextField()
    image = models.ImageField(upload_to='noticias/')
    Voo = models.ForeignKey(Voo, on_delete=models.CASCADE)
    usuario = models.ForeignKey( UserBlog, on_delete=models.CASCADE, blank=True,null=True)  
    

    