from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ("id", "url", "name", "author", "price", "date")


