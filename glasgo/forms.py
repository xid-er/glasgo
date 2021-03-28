from django import forms
from django.contrib.auth.models import User
from glasgo.models import UserProfile, Post, Comment


class PostForm(forms.ModelForm):
    # TODO
    pass

class CommentForm(forms.ModelForm):
    # TODO
    pass


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # describes additional properties about the particular class to which it belongs
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'website', 'picture', 'age', 'occupation', 'university', 'company')
