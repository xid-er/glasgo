import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True, verbose_name="Profile Picture")
    age = models.PositiveIntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=32, blank=True)
    university = models.CharField(max_length=32, blank=True)
    company = models.CharField(max_length=32, blank=True)
    # terms_accepted = models.BooleanField()


    # user can like/favorite many posts
    # and also posts can be liked/favorited by many users
    # posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
       super(UserProfile, self).save(*args, **kwargs)


class Post(models.Model):
    # TODO User Likes/Favorites Post

    # link Post to its owner
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    # attributes
    # https://towardsdatascience.com/build-a-social-media-website-with-django-feed-app-backend-part-4-d82facfa7b3
    post_date_time = models.DateTimeField(default=timezone.now, blank=True)
    post_title = models.CharField(max_length = 128)
    post_type = models.CharField(max_length=64)
# https://stackoverflow.com/questions/16925129/generate-unique-id-in-django-from-a-model-field
    post_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Content of each type of post
    post_text = models.CharField(max_length=2048, blank=True)
    post_pic = models.ImageField(upload_to='post_images', blank=True)
    post_link = models.URLField(blank=True)

    post_category = models.CharField(max_length=64)
    post_likes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.request_id = str(uuid.uuid4().int)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    # link comment to its creator
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # link to post that was commented
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # attributes
    comment_date_time = models.DateTimeField(default=timezone.now)
    comment_content = models.CharField(max_length=1024)

    def __str__(self):
        return self.comment_content

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

class Favourite(models.Model):
    user = models.ForeignKey(User, related_name='favourites', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='favourites', on_delete=models.CASCADE)
