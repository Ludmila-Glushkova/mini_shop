from django.urls import path
from . import views


app_name = 'about'

urlpatterns = [
    path('author/', views.AboutAuthor.as_view(), name='author'),
]
