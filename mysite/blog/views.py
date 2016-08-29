from django.shortcuts import render, render_to_response
from models import Post, Tag
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    post_list = Post.objects.all()
    context = {
        "post_list": post_list
    }
    return render(request, 'blog/index.html', context)


def detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'blog': blog})


def tag_list(request, tag):
    tag_object = get_object_or_404(Tag, title=tag)
    post_list = Post.objects.filter(tags__in=[tag_object.id])
    context = {
        "post_list": post_list
    }
    return render(request, 'blog/index.html', context)
