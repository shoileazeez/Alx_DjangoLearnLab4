from django.urls import path
from . import views
from .views import list_books , LibraryDetailView

urlpatterns = [
    path('books/', views.list_books, name='book-list'),
    path('Detailview/', views.LibraryDetailView.as_view, name='deatilview'),
]


# from django.urls import path
# from .views import book_list_view

# urlpatterns = [
#     path('books/', book_list_view, name='book-list'),
# ]
