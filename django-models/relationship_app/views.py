# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# # relationship_app/views.py
# from django.contrib.auth.views import LoginView
# # relationship_app/views.py
# from django.contrib.auth.views import LogoutView

# class CustomLoginView(LoginView):
#     template_name = 'relationship_app/login.html'
# class CustomLogoutView(LogoutView):
#     template_name = 'relationship_app/logout.html'    

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')  # Adjust 'home' to your desired redirect URL
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# relationship_app/views.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Helper functions to check user roles
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarians'

def is_member(user):
    return user.userprofile.role == 'Member'

# Views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



