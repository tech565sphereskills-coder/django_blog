from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog


def home(request):
    featured_post = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    post = Blog.objects.filter(is_featured=False, status='Published')
    context = {
        'featured_post': featured_post,
        'post': post,
    }
    return render(request, 'home.html', context)
