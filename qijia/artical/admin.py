from django.contrib import admin

from .models import Category, Tag, Artical
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time']
    fields = ('name', )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time']
    fields = ('name', )

@admin.register(Artical)
class ArticalAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_time', 'uv']
    fields = (
        'title',
        'desc',
        ('author', 'category', 'tags'),
        'text',
    )
    search_fields = ['title', 'tags', 'created_time']