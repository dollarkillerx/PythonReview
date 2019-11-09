from django.urls import path
from .views import Music
urlpatterns = [
    path('',Music.as_view())
]