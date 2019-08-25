from django.contrib import admin
from blog import models

# Register your models here.


class PostModel(admin.ModelAdmin):
    list_display = ['title','created_time','category']
    list_filter = ['title','created_time','category']
    search_fields = ['title','article','category']


class CategoryModel(admin.ModelAdmin):
    list_display = ['category']
    list_filter = ['category']
    search_fields = ['category']

class FeelingsModel(admin.ModelAdmin):
    list_display = ['feelings_id','title','textarea']

class CommentModel(admin.ModelAdmin):
    list_display = ['blog','name','email','comment_time','comment_content']
    list_filter = ['blog','name','email','comment_time','comment_content']
    search_fields = ['blog','name','email','comment_time','comment_content']
    ordering = ['-comment_time']

admin.site.register(models.Post,PostModel)
admin.site.register(models.Feelings,FeelingsModel)
admin.site.register(models.Category,CategoryModel)
admin.site.register(models.Comment,CommentModel)