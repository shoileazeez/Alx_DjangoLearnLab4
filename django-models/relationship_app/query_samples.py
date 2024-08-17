# query_samples.py

# from relationship_app.models import Author, Book, Library, Librarian

# def query_books_by_author(author_name):
#     """
#     Query all books by a specific author.
#     """
#     try:
#         author = Author.objects.get(name=author_name)
#         books = Book.objects.filter(author=author)
#         return books
#     except Author.DoesNotExist:
#         return None

# def list_all_books_in_library(library_name):
#     """
#     List all books in a specific library.
#     """
#     try:
#         library = Library.objects.get(name=library_name)
#         books = library.books.all()
#         books.all()
#         return books
#     except Library.DoesNotExist:
#         return None

# def retrieve_librarian_for_library(library_name):
#     """
#     Retrieve the librarian from a specific library.
#     """
#     try:
#         library = Library.objects.get(name=library_name)
#         librarian = Librarian.objects.get(library=library)
#         # Librarian.objects.get(library)
#         return librarian
#     except Library.DoesNotExist:
#         return None
