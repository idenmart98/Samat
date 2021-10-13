from django.contrib import admin
from django.urls import path,include

from .views import ImagesListCreateView

urlpatterns = [
    path('images/', ImagesListCreateView.as_view()),

]