from django.contrib import admin
from blog.models import Post, Comment, Recomment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment

class RecommentInline(admin.TabularInline):
    model = Recomment

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'create_dt']
    list_display_links = ['id', 'title']
    list_filter = ['create_dt', 'author']
    search_fields = ['title', 'author']
    inlines = [
        CommentInline,
        RecommentInline,
    ]

    @admin.register(Comment)
    class CommentAdmin(admin.ModelAdmin):
        list_display = ('id', 'post', 'content', 'author')

    @admin.register(Recomment)
    class RecommentAdmin(admin.ModelAdmin):
        list_display = ('id', 'comment', 'content', 'author')
