from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment 
    extra = 5

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

admin.site.register(Comment)
admin.site.register(Article, ArticleAdmin)

# Register your models here.
