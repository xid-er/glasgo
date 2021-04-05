import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'glasgo_project.settings')
import django
django.setup()
from glasgo.models import UserProfile, Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import random


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

    # not sure if the implemented lists of dictionaries is correct.
    # feel free to modify it.
    post_requests = [
        {'title': 'UofG looks like Hogwarts in the snow',
         'post_category': 'image',
         'post_number': 1,
         'likes': 42,
         },
        {'title': 'Hot Milk is coming to Glasgow on June 14th.',
         'post_category': 'text',
         'post_number': 2,
         'likes': 64
         },
        {'title': "There's new cafe opening up on Dumbarton",
         'post_category': 'video',
         'post_number': 3,
         'likes': 128
         },
        ]

# still need lists of dictionaries

# implement users to test the website into a user_list
# and print the confirm message to guarantee user has been added
    user_list = []
    for us in test_users:
        user_add = add_user(us['username'], us['password'], us['age'],
                            us['occupation'])
        user_list.append(user_add)
        print(f'added example users {user_add}')

# generate some example users with the random first name.


def get_random_name(attribute):
    if attribute == "first":
        first_names = ['Cierra', 'Kierra', 'Thomas', 'Alvaro', 'Miranda',
                        'David', 'Paul', 'Abel', 'Byron', 'Mina', 'Eli', 'Christian']
        return random.choice(first_names)


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
    return user_add


if __name__ == '__main__':
    print('Starting Glasgo population script...')
    populate()

