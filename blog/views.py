from django.shortcuts import render

# Create your views here.
# CHEN added 02/09/2018
def post_list(request):
	return render(request, 'blog/post_list.html', {})
