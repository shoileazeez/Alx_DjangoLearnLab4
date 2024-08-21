from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Article

@permission_required('bookshelf.can_view', raise_exception=True)
def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'bookshelf/view_article.html', {'article': article})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    # Logic to create an article
    return render(request, 'bookshelf/create_article.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # Logic to edit the article
    return render(request, 'bookshelf/edit_article.html', {'article': article})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # Logic to delete the article
    return render(request, 'bookshelf/delete_article.html')



def search_articles(request):
    query = request.GET.get('q', '')
    results = Article.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/search_results.html', {'results': results})

# Create your views here.
