from django.db import models

class SampleModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.DateField()
