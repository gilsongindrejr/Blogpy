from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Slug is in admin page only for debug purposes
    list_display = ('title', 'author', 'status', 'slug')
    list_filter = ('status', 'published', 'author')
    ordering = ('status',)
    autocomplete_fields = ('author',)
    search_fields = ('title', 'body', 'author')
    date_hierarchy = 'published'
    prepopulated_fields = {'slug': ('title',)}
