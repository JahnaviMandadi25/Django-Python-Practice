
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Descending order by creation date
    return render(request, 'post_list.html', {'posts': posts})




def about_me(request):
    return render(request, 'about_me.html')



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})
