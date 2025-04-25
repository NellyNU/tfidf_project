from django.urls import path
from .views import tfidf_view

urlpatterns = [
    path('', tfidf_view, name='tfidf'),
]
