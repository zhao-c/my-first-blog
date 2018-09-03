from django.shortcuts import render
# in order to take models to views, need to include Post class
# CHEN added
from .models import Post
# for filter
from django.utils import timezone

# added 09/03/2018
from django.shortcuts import get_object_or_404

# Create your views here.
# CHEN added 02/09/2018
def post_list(request):
	# posts var points to the datas from the DB
	# add - in 'published_date' for posting the lasted post first
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts' : posts})

# added 09/03/2018
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
