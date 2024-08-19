# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import render

# def is_librarian(user):
#     return user.is_authenticated and user.userprofile.role == 'Librarian'


# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'templates/relationship_app/librarian_view.html')

# from django.shortcuts import render
# from django.contrib.auth.decorators import user_passes_test

# @user_passes_test(lambda u: u.userprofile.role == 'Librarian')
# def librarian_view(request):
#     return render(request, 'librarian_view.html')




# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import render


# def is_librarian(user):
#     return user.userprofile.role == 'Librarians'


# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# librarian_view.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import UserProfile  # Assuming you have UserProfile model linked to User

def is_librarian(user):
    # Check if the user is authenticated and has the role 'Librarian'
    try:
        return user.is_authenticated and user.userprofile.role == 'Librarian'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_librarian, login_url='/login/', redirect_field_name=None)
def librarian_view(request):
    # View logic here
    return render(request, 'librarian_template.html')  # Render a template for librarians

