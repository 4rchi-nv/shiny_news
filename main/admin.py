from django.contrib import admin
from .models import Category,News,Comment,Work

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display=('title','category','add_time')

admin.site.register(News,AdminNews)
admin.site.register(Work,AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display=('news','email','comment','status')
admin.site.register(Comment,AdminComment)
