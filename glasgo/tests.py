from django.test import TestCase
from glasgo.models import UserProfile
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

def get_template(path_to_template):
    """
    Helper function to return the string representation of a template file.
    """
    f = open(path_to_template, 'r')
    template_str = ""
    for line in f:
        template_str = f"{template_str}{line}"

    f.close()
    return template_str





class UserProfileMethodTests(TestCase):
        
    def test_ensure_age_can_be_empty(self):
        """
        Ensures the age of a User Profile can be None/Null.
        """
        up = create_simple_User_Profile_object()
        self.assertEqual((up.age == None), True, f"{FAILURE_HEADER}User Profile age should be allowed to be null. {FAILURE_FOOTER}")
      
    def test_ensure_UserProfile_occupation_can_be_blank(self):
        up = create_simple_User_Profile_object()
        
        """
        Ensures the occupation of a User Profile can be empty.
        """
        self.assertEqual((up.occupation == ''), True, f"{FAILURE_HEADER}User Profile occupation should be allowed to be blank. {FAILURE_FOOTER}")
        
    def test_ensure_UserProfile_university_can_be_blank(self):
        up = create_simple_User_Profile_object()
        """
        Ensures the university of a User Profile can be empty.
        """
        self.assertEqual((up.university == ''), True, f"{FAILURE_HEADER}User Profile university should be allowed to be blank. {FAILURE_FOOTER}")
        
    def test_ensure_UserProfile_company_can_be_blank(self):
        up = create_simple_User_Profile_object()
        """
        Ensures the company of a User Profile can be empty.
        """
        self.assertEqual((up.company == ''), True, f"{FAILURE_HEADER}User Profile company should be allowed to be blank. {FAILURE_FOOTER}")
        



    