from django.contrib import admin

from .models import FirstPage, SiteMap, FriLink
# Register your models here.

@admin.register(FirstPage)
class FirstPageAdmin(admin.ModelAdmin):
    list_display = ('status', 'introduction')
    fields = ('status', 'img', 'introduction', 'category')

@admin.register(SiteMap)
class SiteMapAdmin(admin.ModelAdmin):
    list_display = ('total', 'follow', 'pv')
    fields = ('status', 'total', 'follow', 'pv')

@admin.register(FriLink)
class FriLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    fields = ('status', 'img', 'name', 'link')