from django.urls import path
from .views import Music,Book
urlpatterns = [
    path('music/',Music.as_view()),
    path('book/',Book.as_view())
]