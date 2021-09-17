from django_filters.rest_framework import DjangoFilterBackend
from .models import Books
from .serializer import BooksSerializer
from rest_framework import viewsets, filters

# Created FSOapp views here.
class BooksListView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('name', 'author')
    search_fields = ('name', 'author', 'date')
    ordering_fields = ('price',)



