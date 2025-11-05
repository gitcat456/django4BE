from django.contrib import admin
from .models import Post

# Customize how Post appears in admin
class PostAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ['id', 'title', 'is_published', 'created_at']
    
    # Add search functionality
    search_fields = ['title', 'content']
    
    # Add filters in the sidebar
    list_filter = ['is_published', 'created_at']
    
    # Make fields editable directly from list view
    list_editable = ['is_published']
    
    # Pagination - show 20 items per page
    list_per_page = 20

# Register with custom options
admin.site.register(Post, PostAdmin)