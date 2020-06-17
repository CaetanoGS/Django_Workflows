from django.db import models

class WorkFlow(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    steps = models.TextField()

    #python3 manage.py migrate --run-syncdb



