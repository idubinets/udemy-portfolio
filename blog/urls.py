from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloglist, name='bloglist'),
    path('<int:blog_id>', views.blogdetail, name='blog_detail')
] 