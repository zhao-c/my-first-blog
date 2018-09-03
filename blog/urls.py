from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	# CHEN added a url, create a page for a post. 09/03/2018
	# the name 'post_detail' is equal to the Django template tag added in 'blog/post_list.html'
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	# Added for django form
	# Just now forgot to add / at the end of 'post/new'
	path('post/new/', views.post_new, name='post_new'),
	# Added for editing an existing post
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]