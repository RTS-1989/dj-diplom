from django.contrib import admin
from .models import Category, Subcategory, Product, Review
from .forms import UserReviewAddForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'price', 'available',
        'created', 'updated'
    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','text', 'created', 'moderation']
    list_filter = ['user', 'created', 'moderation']
