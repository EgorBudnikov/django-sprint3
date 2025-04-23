from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .constants import Count_posts
from .models import Category, Post


def get_posts():
    query_post = Post.objects.select_related(
        'category', 'author', 'location'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    return query_post


def index(request):
    """Главная страница - последние опубликованные посты"""
    post_list = get_posts()[:Count_posts]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Cтраница поста"""
    post = get_object_or_404(
        get_posts(),
        pk=post_id,
    )
    context = {
        'post': post,
    }

    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Посты категории с проверкой"""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)

    post_list = get_posts().filter(category=category)

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
