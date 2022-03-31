from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post, PostImage

def photo_list(request):
    posts = Post.objects.all
    return render(request, 'gallery/photo_list.html', {'posts': posts})

def detail_view (request, pk):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'gallery/single_list.html', {'post': post, 'photos': photos})

