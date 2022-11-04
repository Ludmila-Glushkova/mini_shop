from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        '<int:product_id>/comment/',
        views.add_comment, name='add_comment'
    ),
    path('sort/', views.sort, name='sort'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
