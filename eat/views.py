from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Area
import random

def index(request):
    post_list = Area.objects.all()
    return render(request, 'eat/index.html', {'post_list': post_list})


def detail(request):
    place = request.GET.get('place')
    random_idlist = Post.objects.values_list('pk', flat=True)
    random_id = random.randint(1, len(random_idlist))
    post = get_object_or_404(Post, pk=random_id)
    # post = Post.objects.filter(area__area=place)
    # if not post_list:
    #     post_list = Post.objects.filter(body__icontains=q)
    #     return render(request, 'novel/search.html', {'post_list': post_list})

    return render(request, 'eat/detail.html', {'post': post})
