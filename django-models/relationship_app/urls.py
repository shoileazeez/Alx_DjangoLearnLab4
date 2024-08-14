from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('Detailview/', views.BookDetailView.as_view, name='deatilview'),
]


# from django.urls import path
# from .views import book_list_view

# urlpatterns = [
#     path('books/', book_list_view, name='book-list'),
# ]
