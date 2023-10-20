from django.urls import path
from crud.views import article_func,article_detail, article_create, article_edit, article_delate

urlpatterns=[
    path('' , article_func , name="article_func"),
    path('<slug>', article_detail, name='article_detail'),
    path('article_create/', article_create, name='article_create'),
    path('<slug>/edit', article_edit, name='article_edit'),
    path('<slug>/delate', article_delate, name='article_delate')
]