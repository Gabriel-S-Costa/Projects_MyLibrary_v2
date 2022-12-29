from django.contrib import admin

from .models import Book, Category, Publisher, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "publication_date", "edition", "created_at"]
    search_fields = ["title", "original_title", "publisher__name", "isbn"]
    list_filter = ["title", "category", "edition", "publisher", "author"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at"]
    search_fields = ["name"]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "site", "created_at"]
    search = ["name", "site"]
    list_filter = ["name"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "created_at"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["first_name", "last_name"]
