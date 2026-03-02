from django.contrib import admin
from .models import Category, Blog, Comment, UserProfile

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('title', 'category__category_name', 'status')
    list_editable = ('is_featured',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile)
