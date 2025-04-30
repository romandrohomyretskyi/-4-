from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Category, Image

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Image)
