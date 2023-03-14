from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import viewsets

# viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
