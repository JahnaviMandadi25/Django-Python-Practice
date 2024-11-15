from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'content', 'author', 'slug', 'image')  # Include image field
