from django import forms
from django.contrib.auth.models import User
from glasgo.models import UserProfile, Post, Comment


class PostForm(forms.ModelForm):
    # It is for posting a new post by any user.
    class Meta:
        model = Post
        fields = ['post_title', 'post_content']

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['comment_content']



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # describes additional properties about the particular class to which it belongs
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'website', 'picture', 'age', 'occupation', 'university', 'company']

# The form is for user to edit their email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# The form is for user to edit their profile
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'first_name', 'age', 'occupation', 'university', 'company']
