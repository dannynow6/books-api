from django.db import models

# Models for Books_backend


class Author(models.Model):
    """a model representing book authors"""

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    language = models.CharField(max_length=100, blank=True)

    def __str__(self):
        first = self.first_name.title()
        last = self.last_name.title()
        return f"{last}, {first}"


class Book(models.Model):
    """A model representing a Book"""

    title = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    date_published = models.DateField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, default="D. G.")
    isbn = models.CharField(max_length=50, blank=True)
    publisher = models.CharField(max_length=300, blank=True)
    format = models.CharField(max_length=75, blank=True)
    edition = models.CharField(max_length=50, blank=True)

    def __str__(self):
        author = self.author
        title = self.title.title()
        ed = self.edition
        form = self.format
        date_p = self.date_published

        return f"{title} by {author}, Date Published: {date_p}, Edition: {ed} | format: {form}"
