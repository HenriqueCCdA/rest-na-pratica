from rest_framework.generics import ListAPIView, RetrieveAPIView

from devpro.core.models import Author, Book
from devpro.api2.serializers import AuthorSerializer, BookSerializer


class AuthorList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
