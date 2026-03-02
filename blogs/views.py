from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category, Comment
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
# Create your views here.

def post_by_category(request, category_id):
    # Fetch the posts based on category
    posts = Blog.objects.filter(status='Published', category_id=category_id)
    
    # pagination
    paginator = Paginator(posts, 4) # Show 4 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    context = {
        'page_obj': page_obj,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # related posts
    related_posts = Blog.objects.filter(category=single_blog.category, status='Published').exclude(id=single_blog.id).order_by('-created_at')[:3]

    # comments 
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
        'related_posts': related_posts,
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)