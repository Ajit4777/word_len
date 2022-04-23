from django.urls import path

from .views import (WordGet)
#
#
urlpatterns = [
    path('api/<str:word1>/<str:word2>', WordGet.as_view()),
]