from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'is_published', 'created_at', 'text', 'pub_date',
        'author', 'category', 'location'
    )
    list_editable = (
        'author', 'category', 'location', 'is_published'
    )
    search_fields = (
        'title', 'author__username', 'category__title', 'location__name'
    )
    list_filter = (
        'category',
    )
    empty_value_display = 'Не задано'


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'name',
    )
