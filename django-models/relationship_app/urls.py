from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_list, name='book'),
    path('Detailview/', views.BookDetailView.as_view, name='deatilview'),
]