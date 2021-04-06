
from django.test import TestCase
from glasgo.models import UserProfile, Post, Comment, Like, Favourite
from django.contrib.auth.models import User
import os


FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}Glasgo TEST FAILURE :,({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

f"{FAILURE_HEADER} {FAILURE_FOOTER}"


#Helper Functions appear below
def create_user_object():
    """
    Helper function to create a User object.
    """
    user = User.objects.get_or_create(username='testuser',
                                      first_name='Test',
                                      last_name='User',
                                      email='test@test.co.uk')[0]
    user.set_password('abc123test---')
    user.save()
    return user

def create_simple_User_Profile_object():
    """
    Helper function to create a simple User Profile object.
    """
    up = UserProfile.objects.create(user=create_user_object())
    up.save()
    return up

def create_Super_User_object():
    """
    Helper function to create a Super User.
    """
    return User.objects.create_superuser('super', 'super@test.co.uk', 'superpassword')


class UserProfileMethodTests(TestCase):
        
    def test_ensure_age_can_be_empty(self):
        """
        Ensures the age of a User Profile can be None/Null.
        """
        up = create_simple_User_Profile_object()
        self.assertEqual((up.age == None), True, f"{FAILURE_HEADER}User Profile age should be allowed to be null. {FAILURE_FOOTER}")
      
    def test_ensure_user_profile_occupation_can_be_blank(self):
        up = create_simple_User_Profile_object()
        
        """
        Ensures the occupation of a User Profile can be empty.
        """
        self.assertEqual((up.occupation == ''), True, f"{FAILURE_HEADER}User Profile occupation should be allowed to be blank. {FAILURE_FOOTER}")
        
    def test_ensure_user_profile_university_can_be_blank(self):
        up = create_simple_User_Profile_object()
        """
        Ensures the university of a User Profile can be empty.
        """
        self.assertEqual((up.university == ''), True, f"{FAILURE_HEADER}User Profile university should be allowed to be blank. {FAILURE_FOOTER}")
        
    def test_ensure_user_profile_company_can_be_blank(self):
        up = create_simple_User_Profile_object()
        """
        Ensures the company of a User Profile can be empty.
        """
        self.assertEqual((up.company == ''), True, f"{FAILURE_HEADER}User Profile company should be allowed to be blank. {FAILURE_FOOTER}")
        
class UserProfileTryExceptTests(TestCase):
    
    def test_attempt_negative_age(self):
        try:
            up = UserProfile.objects.create(user=create_user_object(), age =-1)
            self.assertEqual((up.age == '-1'), True, f"{FAILURE_HEADER}User Profile age should not be negative. {FAILURE_FOOTER}")
        except:
            pass
        
    def test_attempt_null_occupation(self):
        try:
            up = UserProfile.objects.create(user=create_user_object(), occupation = None)
            self.assertEqual((up.occupation == None), True, f"{FAILURE_HEADER}User Profile occupation cannot be Null. {FAILURE_FOOTER}")
        except:
            pass
        
    def test_attempt_null_university(self):
        try:
            up = UserProfile.objects.create(user=create_user_object(), university = None)
            self.assertEqual((up.university == None), True, f"{FAILURE_HEADER}User Profile university cannot be Null. {FAILURE_FOOTER}")
        except:
            pass
     
    def test_attempt_null_company(self):
        try:
            up = UserProfile.objects.create(user=create_user_object(), company = None)
            self.assertEqual((up.company == None), True, f"{FAILURE_HEADER}User Profile university cannot be Null. {FAILURE_FOOTER}")
        except:
            pass
       
        
    def test_user_profile_with_no_user(self):
        try:
            up = UserProfile.objects.create(user=None)
            self.assertEqual((up.user == None), True, f"{FAILURE_HEADER}User Profile must have an ascociated User. {FAILURE_FOOTER}")
        except:
            pass
        

class PostTryExceptTests(TestCase):
    def test_attempt_null_post_title(self):
        try:
            post = Post.objects.create(user_name = create_user_object(), post_title = None)
            self.assertEqual((post.title == None), True, f"{FAILURE_HEADER}Post title cannot be Null. {FAILURE_FOOTER}")
        except:
            pass
    
    def test_attempt_null_post_type(self):
        try:
            post = Post.objects.create(user_name = create_user_object(), post_type = None)
            self.assertEqual((post.title == None), True, f"{FAILURE_HEADER}Post type cannot be Null. {FAILURE_FOOTER}")
        except:
            pass
    
    def test_attempt_same_post_uuid(self):
        try:
            post1 = Post.objects.create(user_name = create_user_object())
            post2 = Post.objects.create(user_name = create_user_object(), post_number = post1.post_number)
            self.assertEqual((post1.post_number == post2.post_number), True, f"{FAILURE_HEADER}Post uuid cannot be same as another post's uuid. {FAILURE_FOOTER}")
        except:
            pass
    
    def test_post_with_no_user(self):
        try:
            post = Post.objects.create(user_name = None)
            self.assertEqual((post.user_name == None), True, f"{FAILURE_HEADER}Post cannot have a Null user. {FAILURE_FOOTER}")
        except:
            pass


class CommentTryExceptTests(TestCase):
    def test_comment_with_no_user(self):
        user = create_user_object()
        post = Post.objects.create(user_name = user)
        try:
            comment = Comment.objects.create(user = None, post = post)
            self.assertEqual((comment.user == None), True, f"{FAILURE_HEADER}Comment cannot have a Null user. {FAILURE_FOOTER}")
        except:
            pass
    
    def test_comment_with_no_post(self):
        user = create_user_object()
        try:
            comment = Comment.objects.create(user= user, post = None)
            self.assertEqual((comment.post == None), True, f"{FAILURE_HEADER}Comment cannot have a Null post. {FAILURE_FOOTER}")
        except:
            pass
        
    def test_comment_content_not_null(self):
        user = create_user_object()
        post = Post.objects.create(user_name = user)
        try:
            comment = Comment.objects.create(user = user, post = post, content = None)
            self.assertEqual((comment.content == None), True, f"{FAILURE_HEADER}Comment cannot have Null content. {FAILURE_FOOTER}")
        except:
            pass
        
class LikeTryExceptTests(TestCase):
    def test_like_user_not_null(self):
        user = create_user_object()
        post = Post.objects.create(user_name = user)
        try:
            like = Like.objects.create(user = None, post = post)
            self.assertEqual((like.user == None), True, f"{FAILURE_HEADER}Like cannot have Null user. {FAILURE_FOOTER}")
        except:
            pass
            
    def test_like_post_not_null(self):
        try:
            like = Like.objects.create(user = create_user_object(), post = None)
            self.assertEqual((like.post == None), True, f"{FAILURE_HEADER}Like cannot have Null post. {FAILURE_FOOTER}")
        except:
            pass
    
class FavouriteTryExceptTests(TestCase):
    def test_like_user_not_null(self):
        user = create_user_object()
        post = Post.objects.create(user_name = user)
        try:
            favourite = Favourite.objects.create(user = None, post = post)
            self.assertEqual((favourite.user == None), True, f"{FAILURE_HEADER}Favourite cannot have Null user. {FAILURE_FOOTER}")
        except:
            pass
            
    def test_like_post_not_null(self):
        try:
            favourite = Favourite.objects.create(user = create_user_object(), post = None)
            self.assertEqual((favourite.post == None), True, f"{FAILURE_HEADER}Favourite cannot have Null post. {FAILURE_FOOTER}")
        except:
            pass  