from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
            'title',
            'blog_description',
            'is_active',
            'date',
        ]
