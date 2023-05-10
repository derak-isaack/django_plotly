from django.db import models

# Create your models here.
class Sales(models.Model):
    date = models.DateField()
    revenue = models.IntegerField()

    class Meta:
        ordering = ('date',)


