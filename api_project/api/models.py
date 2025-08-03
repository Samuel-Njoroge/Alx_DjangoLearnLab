from django.db import models

# Book
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} by {self.author}"

    #class Meta:
