import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'glasgo_project.settings')

import django
django.setup()
from glasgo.models import UserProfile, Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def populate():

    '''
    Provided test users for testing the features of Glasgo website.
    '''
    test_users = [
        {'username': 'Billy',
         'password': 'billy12345',
         'age': 42,
         'occupation': 'Partner in Law Firm'},
        {'username': 'Katie',
         'password': 'katie12345',
         'age': 12,
         'occupation': 'student'},
        {'username': 'Events4people',
         'password': 'events12345',
         'occupation': 'company'},
    ]

    # still need lists of dictionaries


def make_post(post_title, post_content):
    post = Post.objects.get_or_create(posts_title=post_title, post_content=post_content)[0]
    post.save()
    return post
    
    
def leave_comment(post, comment_content):
    comment = Comment.objects.get_or_create(comment_content=comment_content, post=post)[0]
    comment.save()
    return comment
    
def add_user(first_name, password):
    user_add = User(username=first_name, password=make_password(password))
    user_add.save()
    user_profile = UserProfile.objects.get_or_create(user=user_add)[0]
    user_profile.save()
    return user_to_add

if __name__ == '__main__':
    print('Starting Glasgo population script...')
    populate()
    
