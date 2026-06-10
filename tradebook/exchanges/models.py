from django.db import models

# Create your models here.


class Exchange(models.Model):

    name = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
