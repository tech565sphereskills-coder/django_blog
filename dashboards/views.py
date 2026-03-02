from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from blogs.models import Category, Blog
from .forms import CategoryForm, BlogForm, EditUserForm, AddUserForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()

    context = {
        'category_count': category_count,
        'blog_count': blog_count,
    }
    return render(request, 'dashboards/dashboard.html', context)


@login_required(login_url='login')
def category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'dashboards/category.html', context)


@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboards/add_category.html', context)


@login_required(login_url='login')
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboards/edit_category.html', context)


@login_required(login_url='login')
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category')


@login_required(login_url='login')
def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboards/posts.html', context)


@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save() # ID is generated here
            post.slug = slugify(post.title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)
    form = BlogForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboards/add_post.html', context)


@login_required(login_url='login')
def edit_post(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form = BlogForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboards/edit_post.html', context)


@login_required(login_url='login')
def delete_post(request, id):
    post = get_object_or_404(Blog, id=id)
    post.delete()
    return redirect('posts')


@login_required(login_url='login')
def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'dashboards/users.html', context)


@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = AddUserForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboards/add_user.html', context)


@login_required(login_url='login')
def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'dashboards/edit_user.html', context)


@login_required(login_url='login')
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users')
