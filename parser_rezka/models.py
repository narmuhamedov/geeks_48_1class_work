from django.db import models


class RezkaParser(models.Model):
    title = models.CharField(max_length=100)
    href = models.URLField()
    
    def __str__(self):
        return self.title
