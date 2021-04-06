import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'glasgo_project.settings')
import django
django.setup()
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.core.files import File

from glasgo.models import UserProfile, Post, Comment
import random
import urllib.request


def populate():

    '''
    Provided test users for testing the features of Glasgo website.
    '''
    test_users = [
        {'username': 'Billy',
         'password': 'billy12345',
         'age': 42,
         'occupation': 'E',
         'company': 'Definitely Real Law Firm',
         'university': None},
        {'username': 'Katie',
         'password': 'katie12345',
         'age': 12,
         'occupation': 'S',
         'university': None,
         'company': None},
        {'username': 'Events4people',
         'password': 'events12345',
         'occupation': 'E',
         'company': 'Events4People',
         'university': None,
         'age': None},
        {'username': 'kokomo4ever',
         'password': 'Qwerty123*',
         'age' : 23,
         'occupation': 'E',
         'company': 'Freelancer',
         'university': None},
        {'username': 'mitochondria',
         'password': 'StemCells000',
         'age': 30,
         'occupation': 'S',
         'university': 'University of Glasgow',
         'company': None},
        {'username': 'xxx420xxx',
         'password': 'helloworld123',
         'age': 65,
         'occupation': 'U',
         'company': None,
         'university': None}

    ]

    # winter = os.path.join(examples, 'uofg-winter.png')
    # implement users to test the website into a user_list
    # and print the confirm message to guarantee user has been added
    user_list = []
    user_list.append(User.objects.create_superuser('admin', 'karlis.siders@gmail.com', 'glasgo123'))
    for us in test_users:
        user_add = add_user(us['username'], us['password'], us['occupation'], us['university'], us['company'], us['age'])
        user_list.append(user_add)
        print(f'added example user {user_add}')

    posts = [
        {'title': 'UofG looks like Hogwarts in the snow',
         'post_pic': None,
         'post_text': None,
         'post_link': None,
         'user': random.choice(user_list),
         'post_type': 'IMG',
         'likes': 42,
         'post_category': 'SoG'
         },
        {'title': 'Hot Milk is coming to Glasgow on June 14th.',
         'post_text': 'After 10 years we are coming back to our most favourite city in Glasgow! Special offer for first 10 customers: pay 2, get 3 drinks!',
         'post_link': None,
         'post_pic': None,
         'user': random.choice(user_list),
         'post_type': 'TXT',
         'likes': 64,
         'post_category': 'CS'
         },
        {'title': "There's new cafe opening up on Dumbarton",
         'post_text': 'I spotted this new spot while coming home from my lectures, it is super cute! Definitelly worth to stop by!',
         'post_link': None,
         'post_pic': None,
         'user': random.choice(user_list),
         'post_type': 'TXT',
         'likes': 128,
         'post_category': 'SoG'
         },
        {'title': "Kilo Sale at Glasgow Green!",
         'post_text': 'Coming back with more clothes and accessories than ever before! This May, Kilo Sale will return to Glasgow and you do not want to miss it! Date TBD',
         'post_link': None,
         'post_pic': None,
         'user': random.choice(user_list),
         'post_type': 'TXT',
         'likes': 5,
         'post_category': 'EVE'
         },
        {'title': "!!Annual Reggaeton Summer Festival Cancelled!!",
         'post_text': 'Due to a specific virus outbreak, we are sorry to announce that Reggaeton Festival is postponed for next year.',
         'post_link': None,
         'post_pic': None,
         'user': random.choice(user_list),
         'post_type': 'TXT',
         'likes': 10,
         'post_category': 'EVE'
         },
        {'title': "Hot Milk is coming to Glasgow on June 14th!",
         'post_link': urllib.request.urlopen('https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
         'post_text': None,
         'post_pic': None,
         'user': random.choice(user_list),
         'post_type': 'URL',
         'likes': 420,
         'post_category': 'EVE'
         }
        ]




    for post in posts:
        add_post(post['user'], post['title'], post['post_type'], post['post_category'],
                 post['post_text'], post['post_link'], post['post_pic'],
                 post['likes'])

# generate some example users with the random first name.


def get_random_name(attribute):
    if attribute == "first":
        first_names = ['Cierra', 'Kierra', 'Thomas', 'Alvaro', 'Miranda',
                        'David', 'Paul', 'Abel', 'Byron', 'Mina', 'Eli', 'Christian']
        return random.choice(first_names)


def add_post(user_name, post_title, post_type, post_category, post_text, post_link,
             post_pic, post_likes, post_date_time=timezone.now()):
    post = Post.objects.get_or_create(user_name=user_name, post_type=post_type,
                                      post_category=post_category,
                                      post_title=post_title, post_text=post_text,
                                      post_link=post_link, post_pic=post_link,
                                      post_likes=post_likes,
                                      post_date_time=post_date_time)[0]
    post.save()
    return post


def add_comment(user, post, comment_content, comment_date_time=timezone.now):
    comment = Comment.objects.get_or_create(user=user, post=post, comment_content=comment_content, comment_date_time=comment_date_time)[0]
    comment.save()
    return comment


def add_user(user_name, password, occupation, university, company, age=0):
    user_add = User(username=user_name, password=make_password(password))
    user_add.save()
    user_profile = UserProfile.objects.get_or_create(user=user_add, age=age, occupation=occupation)[0]
    user_profile.save()
    return user_add


if __name__ == '__main__':
    print('Starting GlasGO population script...')
    populate()
