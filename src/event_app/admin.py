from django.contrib import admin

from .models import Link,Post

class LinkAdmin(admin.StackedInline):
    model = Link

@admin.register(Post)
class NewsAdmin(admin.ModelAdmin):

    list_display = ("title", "description","category","author","phone")
    inlines = [LinkAdmin]
    list_display_links = ("title",)
