from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    empty_value_display = 'unknown'
    list_display = ['title','author', 'status', 'published_date', 'creation_date']
    list_filter = ('status','author',)
    search_fields = ['title', 'content']
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
