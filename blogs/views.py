from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def post_by_category(request, category_id):
    # fetch the posts that belongs to the category with the id category_id 
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id) 

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)