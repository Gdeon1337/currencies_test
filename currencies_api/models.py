from django.db import models


class Currencies(models.Model):
    title = models.CharField(max_length=16)
    ruble_rate = models.FloatField()

    def __str__(self):
        return self.title
