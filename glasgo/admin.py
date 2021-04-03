from django.contrib import admin
from glasgo.models import UserProfile, Post, Comment, Like, Favourite

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Favourite)
