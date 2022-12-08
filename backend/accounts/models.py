from django.db import models
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"


