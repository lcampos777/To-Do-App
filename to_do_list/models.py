from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title