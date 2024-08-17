# from django.urls import path
# from . import views
# from .views import list_books, LibraryDetailView

# urlpatterns = [
#     path('', views.list_books, name='book-list'),
#     path('Detailview/', views.LibraryDetailView, name='deatilview'),
# ]


# from django.urls imyou can 

# urlpatterns = [
#     path('books/', book_list_view, name='book-list'),
# ]

# relationship_app/urls.py
# from django.urls import path
# from .views import CustomLoginView, CustomLogoutView, register

# urlpatterns = [
#     path('login/', CustomLoginView.as_view(), name='login'),
#     path('logout/', CustomLogoutView.as_view(), name='logout'),
#     path('register/', register, name='register'),
#     path('views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=')
# ]


# relationship_app/urls.py
from django.urls import path
from . import views
from . import librarian_view
from . import Member_view
# from .views import admin_view, librarian_view,  member_view

urlpatterns = [
    path('admins', views.admin_view, name='admins'),
    path('librarians', librarian_view.librarian_view, name='librarians'),
    path('members', Member_view.member_view, name='members'),
]

# relationship_app/urls.py
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),
]


# views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=