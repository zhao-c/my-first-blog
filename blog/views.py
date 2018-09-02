from django.shortcuts import render
# in order to take models to views, need to include Post class
# CHEN added
from .models import Post
# for filter
from django.utils import timezone

# Create your views here.
# CHEN added 02/09/2018
def post_list(request):
	# posts var points to the datas from the DB
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts' : posts})
