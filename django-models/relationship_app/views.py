# # from django.shortcuts import render, redirect
# # from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth import login
# # # relationship_app/views.py
# # from django.contrib.auth.views import LoginView
# # # relationship_app/views.py
# # from django.contrib.auth.views import LogoutView

# # class CustomLoginView(LoginView):
# #     template_name = 'relationship_app/login.html'
# # class CustomLogoutView(LogoutView):
# #     template_name = 'relationship_app/logout.html'    

# # def register(request):
# #     if request.method == 'POST':
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             login(request, user)
# #             return redirect('home')  # Adjust 'home' to your desired redirect URL
# #     else:
# #         form = UserCreationForm()
# #     return render(request, 'relationship_app/register.html', {'form': form})

# # relationship_app/views.py
# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import render
# # from .models import UserProfile

# # def is_librarian(user):
# #     # Check if the user is authenticated and has the role 'Librarian'
# #     try:
# #         return user.is_authenticated and user.userprofile.role == 'Librarian'
# #     except UserProfile.DoesNotExist:
# #         return False

# # @user_passes_test(is_librarian, login_url='/login/', redirect_field_name=None)
# # def librarian_view(request):
# #     # View logic here
# #     return render(request, 'librarian_template.html')  # Render a template for librarians



# def is_librarian(user):
#     # return user.is_authenticated and user.userprofile.role == 'Librarians'
#     return user.userprofile.role == 'Librarian'

# def is_member(user):
#     return user.userprofile.role == 'Member'



# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')



# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import render


# def is_librarian(user):
#     return user.is_authenticated and user.userprofile.role == 'Librarian'


# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')



# # relationship_app/views.py
# from django.contrib.auth.decorators import permission_required
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Book
# from . import BookForm  # Assuming you have a form for Book

# @permission_required('relationship_app.can_add_book', raise_exception=True)
# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')  # Adjust 'book_list' to your desired redirect URL
#     else:
#         form = BookForm()
#     return render(request, 'relationship_app/add_book.html', {'form': form})

# @permission_required('relationship_app.can_change_book', raise_exception=True)
# def edit_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book_detail', book_id=book.id)  # Adjust as needed
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'relationship_app/edit_book.html', {'form': form})

# @permission_required('relationship_app.can_delete_book', raise_exception=True)
# def delete_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('book_list')  # Adjust as needed
#     return render(request, 'relationship_app/delete_book.html', {'book': book})


# from django.shortcuts import render
# from .models import Book
# from .models import Library
# from django.views.generic.detail import DetailView

# def book_list_view(request):
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})

# from django.views.generic import DetailView


# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'





# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Book
# from django.urls import reverse_lazy
# from django.views.generic.detail import DetailView
# from .models import Library

# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.decorators import permission_required


# def list_books(request):
#     books = Book.objects.all()
#     return render(request, "relationship_app/list_books.html", {'books': books})

# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = "relationship_app/library_detail.html"
#     context_object_name = "library"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = self.object.books.all()  # Assuming the related_name for books in Library model is 'books'
#         return context

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# class LoginView(LoginView):
#     template_name = 'relationship_app/login.html'
#     success_url = reverse_lazy('home')
#     redirect_authenticated_user = True

# class LogoutView(LogoutView):
#     next_page = reverse_lazy('home')

# @login_required
# def home(request):
#     return render(request, 'home.html') # NEEDS WORK



# @user_passes_test(lambda u: u.userprofile.role == 'Admin')
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @user_passes_test(lambda u: u.userprofile.role == 'Librarians')
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @user_passes_test(lambda u: u.userprofile.role == 'Member')
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')

# @permission_required('relationship_app.can_add_book')
# def add_book(request):
#     if request.method == 'POST':
#         pass
#     else:
#         return render(request, 'add_book.html')
    
# @permission_required('relationship_app.can_change_book')
# def edit_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == 'POST':
#         pass
#     else:
#         return render(request, 'edit_book.html', {'book': book})
    
# @permission_required('relationship_app.can_delete_book')
# def delete_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('book_list')
#     else:
#         return render(request, 'confirm_delete.html', {'book': book})
# # Create your views here.

# def is_librarian(user):
#     if user.is_authenticated:
#         return user.userprofile.role == 'Librarians'
#     return False

# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import render

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     # Your view logic here
#     return render(request, 'librarian_template.html')



from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'librarian'


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
