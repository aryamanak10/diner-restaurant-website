from .models import Post, Category, Comment
from django.contrib import admin

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)