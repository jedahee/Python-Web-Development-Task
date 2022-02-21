from django.shortcuts import render
from .models import General, Category, Tag, Post

# Create your views here.


def home(request):
    general = General.objects.first()
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/home.html', {
        'general': general,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })


def category(request, slug):
    general = General.objects.first()
    posts = Post.objects.filter(category__slug = slug)
    requested_category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/category.html', {
        'general': general,
        'posts': posts,
        'category': requested_category,
        'categories': categories,
        'tags': tags,
    })


def tag(request, slug):
    general = General.objects.first()
    posts = Post.objects.filter(tag__slug = slug)
    requested_tag = Tag.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/category.html', {
        'general': general,
        'posts': posts,
        'tag': requested_tag,
        'categories': categories,
        'tags': tags,
    })


def post(request, slug):
    general = General.objects.first()
    requested_post = Post.objects.get(slug=slug)
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    return render(request, 'blog/post.html', {
        'general': general,
        'post': requested_post,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })

def search(request):
    general = General.objects.first()
    query = request.GET.get('q', '')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = []

    return render(request, 'blog/search.html', {
        'general': general,
        'posts': posts,
        'query': query,
        'categories': categories,
        'tags': tags,
    })