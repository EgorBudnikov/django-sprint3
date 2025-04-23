from django.contrib import admin

from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'is_published', 'created_at', 'text', 'pub_date',
        'author', 'category', 'location'
    )
    list_editable = (
        'author', 'category', 'location', 'is_published'
    )
    search_fields = (
        'title', 'location', 'author'
    )
    list_filter = (
        'category',
    )
    empty_value_display = 'Не задано'


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
    )


admin.site.register(Location)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
