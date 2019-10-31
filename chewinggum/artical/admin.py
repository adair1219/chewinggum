from django.contrib import admin

from .models import Tag, Category, Post
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'status', 'created_time',
                    'post_count')

    fields = ('name', 'status', 'owner', 'desc')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'created_time')
    fields = ('name', 'status', 'owner')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_dispaly = (
        'id',
        'title', 'status', 'category',
        'tag', 'created_time',
    )
    fields = [
        ('title', 'category', 'tag'),
        ('status', 'owner', 'img',),
        'content',
    ]

    search_fields = ['title', 'category', 'tag']
