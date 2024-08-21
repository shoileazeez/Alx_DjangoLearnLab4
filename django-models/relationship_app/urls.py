from django.urls import path
from relationship_app import views  # Import views directly
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    
    # Django's built-in views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Custom views
    path('custom_login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('custom_logout/', views.CustomLogoutView.as_view(), name='custom_logout'),

    # Registration view (custom)
    path('register/', views.register, name='register'),

    # Role-based views
    
    
    
    
    # urls.py


    
    
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

