# coding:utf-8
from django.contrib import admin
# Register your models here.
from web.models import *

#自定义
class ArticleAdmin(admin.ModelAdmin):
#通过定义ModelAdmin的媒体文件的方式为文本输入框添加富文本编辑器
    class Media:
        js = (
            '/static/kindeditor-4.1.10/kindeditor-min.js',
            '/static/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/kindeditor-4.1.10/config.js',
        )
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
