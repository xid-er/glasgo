from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=64, unique=True, primary_key=True)
    last_name = models.CharField(max_length=64, unique=True, blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    age = models.PositiveIntegerField(blank=True)
    occupation = models.CharField(max_length=32, blank=True)
    university = models.CharField(max_length=32, blank=True)
    company = models.CharField(max_length=32, blank=True)

    # user can like/favorite many posts
    # and also posts can be liked/favorited by many users
    # posts = models.ManyToManyField(Post)
    # commented out because causes error (Karlis)

    def __str__(self):
        return self.user.username

   # def save(self, *args, **kwargs):
   #     self.slug = slugify(self.name)
   #     super(UserProfile, self).save(*args, **kwargs)


class Post(models.Model):
    # TODO User Likes/Favorites Post

    # link Post to it's owner
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # attributes
    slug = models.SlugField(unique=True)
    post_date_time = models.DateTimeField(blank=True)
    post_title = models.CharField(max_length = 128)
    post_number = models.IntegerField(unique=True)
    post_type = models.CharField(max_length=64)
    post_content = models.CharField(max_length=2048)
    post_category = models.CharField(max_length=64)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.post_content


class Comment(models.Model):
    # link comment to it's creator
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # link to post that was commented
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # attributes
    comment_date_time = models.DateTimeField(blank=True)
    comment_content = models.CharField(max_length=1024)

    def __str__(self):
        return self.comment_content
