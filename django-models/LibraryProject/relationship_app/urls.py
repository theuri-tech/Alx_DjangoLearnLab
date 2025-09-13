from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import  list_books, LibraryDetailView
from . import views
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path("add_book/", views.add_book_view, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book_view, name="edit_book"),
    path('delete-book/<int:book_id>/', views.delete_book_view, name='delete_book'),
]