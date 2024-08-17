from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# relationship_app/views.py
from django.contrib.auth.views import LoginView
# relationship_app/views.py
from django.contrib.auth.views import LogoutView

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Adjust 'home' to your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


