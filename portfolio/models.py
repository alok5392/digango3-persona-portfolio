from django.db import models

# Create your models here.

class Project(models.Model):
    """docstring fo Project."""
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
