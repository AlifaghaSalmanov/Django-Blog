from django.contrib import admin

from .models import Article, Comment

admin.site.register(Comment)

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ["id", "title", "author", "created_date"]
    list_display_links = ["title", "author"]
    search_fields = ["title"]
