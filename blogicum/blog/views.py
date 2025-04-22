from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post, Category

now = timezone.now()


def index(request):
    """Главная страница - 5 последних опубликованных постов"""
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        pub_date__lte=now,
        category__is_published=True
    ).order_by('-id')[0:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Cтраница поста"""
    post = get_object_or_404(
        Post,
        Q(pk=post_id)
        & Q(pub_date__lte=now)
        & Q(is_published=True)
        & Q(category__is_published=True)
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

    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        pub_date__lte=now,
        category=category,

    )

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
