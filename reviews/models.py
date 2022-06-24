from django.db import models
from django.contrib.auth.models import User

class ReviewsModel(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    estreno = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
