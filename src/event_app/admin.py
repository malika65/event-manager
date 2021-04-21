from django.contrib import admin

from .models import Post,PostImage



class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class NewsAdmin(admin.ModelAdmin):

    list_display = ("title", "description","category","author","phone","link_list")
    inlines = [PostImageAdmin]
    list_display_links = ("title",)

