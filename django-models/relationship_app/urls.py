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
from . import member_view
# from .views import admin_view, librarian_view,  member_view

urlpatterns = [
    path('admins', views.admin_view, name='admin_view'),
    path('librarians', librarian_view.librarian_view, name='librarian_view'),
    path('members', member_view.member_view, name='member_view'),
]

# relationship_app/urls.py
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),
]
# add_book/", "edit_book/

# views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=


from django.urls import path
from .views import book_list_view, LibraryDetailView

urlpatterns = [
    path('books/', book_list_view, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]
