from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

#auto_now_add indica que se agregará la fecha cuando se crea el registro
#auto_now indica que ese campo se modificará cuando se haga un cambio a un registro existente