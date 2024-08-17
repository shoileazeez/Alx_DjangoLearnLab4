from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'templates/relationship_app/librarian_view.html')

# from django.shortcuts import render
# from django.contrib.auth.decorators import user_passes_test

# @user_passes_test(lambda u: u.userprofile.role == 'Librarian')
# def librarian_view(request):
#     return render(request, 'librarian_view.html')