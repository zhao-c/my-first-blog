from django.shortcuts import render
# in order to take models to views, need to include Post class
# CHEN added
from .models import Post
# for filter
from django.utils import timezone

# added 09/03/2018
from django.shortcuts import get_object_or_404
# for Django form
from .forms import PostForm
# after writing a post and save it, redrect to the single post page: post_detail.html
from django.shortcuts import redirect

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

# after adding new url in 'blog/urls.py', need define post_new
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
	
# Added for editing an existing post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
