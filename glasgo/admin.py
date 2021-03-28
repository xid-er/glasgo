from django.contrib import admin
from glasgo.models import UserProfile, Post, Comment

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Post)