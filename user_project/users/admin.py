from django.contrib import admin
from .models import Company, Address, User, Post, Comment, Album, Photo, Todo, Geo

admin.site.register(Company)
admin.site.register(Address)
admin.site.register(Geo)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Todo)