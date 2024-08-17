from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', views.list_books, name='book-list'),
    path('Detailview/', views.LibraryDetailView, name='deatilview'),
]


# from django.urls imyou can 

# urlpatterns = [
#     path('books/', book_list_view, name='book-list'),
# ]
