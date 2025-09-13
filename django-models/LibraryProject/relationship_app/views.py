from django.shortcuts import render

# Create your views here.
from .models import Book, Library
from django.http import HttpResponse

def list_books(request):
    books = Book.objects.all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain") 

from django.views.generic.detail import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    