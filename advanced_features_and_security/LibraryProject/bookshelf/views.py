from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Article

@permission_required('your_app.can_view', raise_exception=True)
def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'your_app/view_article.html', {'article': article})

@permission_required('your_app.can_create', raise_exception=True)
def create_article(request):
    # Logic to create an article
    return render(request, 'your_app/create_article.html')

@permission_required('your_app.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # Logic to edit the article
    return render(request, 'your_app/edit_article.html', {'article': article})

@permission_required('your_app.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # Logic to delete the article
    return render(request, 'your_app/delete_article.html')
# Create your views here.
