from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_table, name='book_table')
]
