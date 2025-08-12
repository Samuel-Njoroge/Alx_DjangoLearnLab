from django.db import models

# Author
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

# Book
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.CharField(max_length=25)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books' 
