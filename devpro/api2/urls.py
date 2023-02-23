from django.urls import path

from . import views


# app_name = 'api2'
urlpatterns = [
    path('author/', views.AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('book/', views.BookList.as_view(), name='book-list'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book-detail')
]
