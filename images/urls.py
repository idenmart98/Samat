from .views import ImageView
from django.urls import path

urlpatterns = [
    path('images/', ImageView.as_view()),
]