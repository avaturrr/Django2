from django.contrib import admin

from manager.models import Book, Comment


# Register your models here.

class CommentInLine(admin.StackedInline):
    model = Comment


class BookAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


admin.site.register(Book, BookAdmin)
admin.site.register(Comment)
