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
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]



# views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=