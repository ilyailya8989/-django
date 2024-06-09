from django.contrib import admin

from jobapp.models import Category, Post, Coment

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Coment)