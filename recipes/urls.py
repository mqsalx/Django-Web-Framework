# flake8: noqa
from django.urls import path
from recipes.views import home


urlpatterns = [
    path('', home), #Home
]
