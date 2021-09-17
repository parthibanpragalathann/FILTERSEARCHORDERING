# Filter, Search and Ordering data in Django Rest Framework

## Created Database in Postgres
## Created and activate virtual environment

## Installed Packages or Dependencies 

````python 
  pip install django, djangorestframework, psycopg2, django-filter
````

## Created API for STORE project and app

````python 
django-admin startproject FSOapi

django-admin startapp FSOapp
````

## Application definition(settings.py)

````python 
INSTALLED_APPS = [
    'app',
    'rest_framework',
    'django_filters',
]
````

## DB Connections (settings.py)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DemoFSO',
        'USER': 'postgres',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## Created models

```doctest
Created app models here.

models -> Books, company and projects
Fields : name, author, price, date
```

## Created  Migrations and Run The server
````python 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```` 

## Created and Added Filter,Search and Order class in viewset
```python 
settings.py

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',
                                'rest_framework.filters.SearchFilter',
                                'rest_framework.filters.OrderingFilter',
                                ]
}

views.py
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
```

## Applications urls

````python API URLS - 
    http://127.0.0.1:8000/api/
    http://127.0.0.1:8000/api/books/
    http://127.0.0.1:8000/api/books/1/
    http://127.0.0.1:8000/api/books/?name=The+Great+Birth&author=Parthiban
    http://127.0.0.1:8000/api/books/?search=The+
    http://127.0.0.1:8000/api/books/?ordering=price&search=The+
````
```
    Result:
    FILTER -
        GET /api/books/?name=The+Great+Birth&author=Parthiban
    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    [
        {
            "id": 5,
            "url": "http://127.0.0.1:8000/api/books/5/",
            "name": "The Great Birth",
            "author": "Parthiban",
            "price": 10000,
            "date": "2021-09-17T14:09:34.220841Z"
        }
    ]
    
    SEARCH -
    
    GET /api/books/?search=The+
        HTTP 200 OK
        Allow: GET, POST, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept
        
        [
            {
                "id": 2,
                "url": "http://127.0.0.1:8000/api/books/2/",
                "name": "Master of The Game",
                "author": "sidney sheldon",
                "price": 500,
                "date": "2021-09-17T14:07:36.097811Z"
            },
            {
                "id": 4,
                "url": "http://127.0.0.1:8000/api/books/4/",
                "name": "The Great Gatsby",
                "author": "Robin",
                "price": 100,
                "date": "2021-09-17T14:09:05.416713Z"
            },
            {
                "id": 5,
                "url": "http://127.0.0.1:8000/api/books/5/",
                "name": "The Great Birth",
                "author": "Parthiban",
                "price": 10000,
                "date": "2021-09-17T14:09:34.220841Z"
            }
        ]
        
    Ordering -
    GET /api/books/?ordering=price&search=The+
    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    [
        {
            "id": 4,
            "url": "http://127.0.0.1:8000/api/books/4/",
            "name": "The Great Gatsby",
            "author": "Robin",
            "price": 100,
            "date": "2021-09-17T14:09:05.416713Z"
        },
        {
            "id": 2,
            "url": "http://127.0.0.1:8000/api/books/2/",
            "name": "Master of The Game",
            "author": "sidney sheldon",
            "price": 500,
            "date": "2021-09-17T14:07:36.097811Z"
        },
        {
            "id": 5,
            "url": "http://127.0.0.1:8000/api/books/5/",
            "name": "The Great Birth",
            "author": "Parthiban",
            "price": 10000,
            "date": "2021-09-17T14:09:34.220841Z"
        }
    ]
    
```
