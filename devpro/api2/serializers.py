from rest_framework import serializers

from devpro.core.models import Author, Book


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name', 'books', 'created_at', 'modified_at')

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'edition', 'publication_year', 'authors', 'created_at', 'modified_at')
