import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'glasgo_project.settings')
import django
django.setup()
from glasgo.models import UserProfile, Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone
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
        {'username': 'kokomo4ever',
         'password': 'Qwerty123*',
         'age' : 23,
         'occupation': 'freelancer'},
        {'username': 'mitochondria',
         'password': 'StemCells000',
         'age': 30,
         'occupation': 'Postgrad in Biochemistry'},

    ]


    posts = [
        {'title': 'UofG looks like Hogwarts in the snow',
         'post_content': '',
         'user': 'Billy',
         'post_type': 'image',
         'post_number': 1,
         'likes': 42,
         'post_category': 'Shot of Glasgow'
         },
        {'title': 'Hot Milk is coming to Glasgow on June 14th.',
         'post_content': 'After 10 years we are coming back to our most favourite city in Glasgow! Special offer for first 10 customers: pay 2, get 3 drinks!',
         'user': 'mitochondria',
         'post_type': 'text',
         'post_number': 2,
         'likes': 64,
         'post_category': 'Cool Spot'
         },
        {'title': "There's new cafe opening up on Dumbarton",
         'post_content': 'I spotted this new spot while coming home from my lectures, it is super cute! Definitelly worth to stop by!',
         'user': 'Katie',
         'post_type': 'text',
         'post_number': 3,
         'likes': 128,
         'post_category': 'Shot of Glasgow'
         },
        {'title': "Kilo Sale at Glasgow Green!",
         'post_content': 'Coming back with more clothes and accessories than ever before! This May, Kilo Sale will return to Glasgow and you do not want to miss it! Date TBD',
         'user': 'Katie',
         'post_type': 'text',
         'post_number': 4,
         'likes': 5,
         'post_category': 'Event'
         },
        {'title': "!!Annual Reggaeton Summer Festival Cancelled!!",
         'post_content': 'Due to a specific virus outbreak, we are sorry to announce that Reggaeton Festival is postponed for next year.',
         'user': 'Events4People',
         'post_type': 'text',
         'post_number': 5,
         'likes': 10,
         'post_category': 'Event'
         },
        ]


# implement users to test the website into a user_list
# and print the confirm message to guarantee user has been added
    user_list = []
    for us in test_users:
        user_add = add_user(us['username'], us['password'], us['age'], us['occupation'])
        user_list.append(user_add)
        print(f'added example users {user_add}')

    for post in posts:
        add_post(post['user'], post['title'], post['post_type'], post['post_category'], post['post_content'],
                 post['likes'], post['post_number'])

# generate some example users with the random first name.


def get_random_name(attribute):
    if attribute == "first":
        first_names = ['Cierra', 'Kierra', 'Thomas', 'Alvaro', 'Miranda',
                        'David', 'Paul', 'Abel', 'Byron', 'Mina', 'Eli', 'Christian']
        return random.choice(first_names)


def add_post(user_name, post_title, post_type, post_category, post_content, post_likes, post_number, post_date_time=timezone.now):
    post = Post.objects.get_or_create(user_name=user_name, post_type=post_type, post_category=post_category,
                                      posts_title=post_title, post_content=post_content, post_likes=post_likes,
                                      post_number=post_number, post_date_time=post_date_time)[0]
    post.save()
    return post


def add_comment(user, post, comment_content, comment_date_time=timezone.now):
    comment = Comment.objects.get_or_create(user=user, post=post, comment_content=comment_content, comment_date_time=comment_date_time)[0]
    comment.save()
    return comment


def add_user(user_name, password, occupation, age=0):
    user_add = User(username=user_name, password=make_password(password))
    user_add.save()
    user_profile = UserProfile.objects.get_or_create(user=user_add, user_name=user_name, age=age, occupation=occupation)[0]
    user_profile.save()
    return user_add


if __name__ == '__main__':
    print('Starting Glasgo population script...')
    populate()

