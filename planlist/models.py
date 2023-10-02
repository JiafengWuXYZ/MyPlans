from django.db import models


# Create your models here.

class Planer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Plan(models.Model):
    planer = models.ForeignKey(Planer, on_delete=models.CASCADE)
    content = models.TextField(blank=False, max_length=256)
    planStartTime = models.DateTimeField()
    planEndTime = models.DateTimeField()
    realStartTime = models.DateTimeField()
    realEndTime = models.DateTimeField()

    def __str__(self):
        return self.content
