from django.shortcuts import render

# Create your views here.
from .models import Book
from django.http import HttpResponse

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render, redirect 

#login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books') #Redirect to protected page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

#logout view
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

#register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #Auto align after registration
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

