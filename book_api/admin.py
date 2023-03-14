from django.contrib import admin
from .models import Author, Book

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list = ("first_name", "last_name", "language")

    admin.site.register(Author)


class BookAdmin(admin.ModelAdmin):
    list = ("author", "title", "publisher", "date_published", "genre")

    admin.site.register(Book)
