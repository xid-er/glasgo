from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import InlineRadios
from glasgo.models import UserProfile, Post, Comment

POST_TYPES = (('TXT', 'Text Post'),
              ('URL', 'Link Post'),
              ('IMG', 'Image Post'))

POST_CATS = (('EVE', 'Event'),
              ('CS', 'Cool Spot'),
              ('SoG', 'Shot of Glasgow'),
              ('O', 'Other'))

class PostForm(forms.ModelForm):
    # It is for posting a new post by any user.
    post_type = forms.ChoiceField(choices=POST_TYPES, widget=forms.RadioSelect)
    post_category = forms.ChoiceField(choices=POST_CATS, widget=forms.RadioSelect)
    class Meta:
        model = Post
        fields = ['post_type', 'post_category', 'post_title', 'post_text', 'post_pic', 'post_link']

# https://stackoverflow.com/questions/37151661/django-crispy-forms-custom-input-positioning-and-inline-radio-buttons
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        helper = self.helper = FormHelper()
        helper.layout = Layout(
            InlineRadios('post_type'),
            InlineRadios('post_category')
        )
        for field_name, field in self.fields.items():
            self.helper.form_show_labels = False
            field.widget.attrs['placeholder'] = field.label

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_content']

class UserForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
    # describes additional properties about the particular class to which it belongs
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

# https://stackoverflow.com/questions/13482753/use-field-label-as-placeholder-in-django-crispy-forms
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        helper = self.helper = FormHelper()

        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            helper.form_show_labels = False
            field.widget.attrs['placeholder'] = field.label

# https://stackoverflow.com/questions/34609830/django-modelform-how-to-add-a-confirm-password-field
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password does not match"
            )

# https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#basic-crispy-form-rendering
OCCUPATION = (('E', 'Employed'),
              ('U', 'Unemployed'),
              ('S', 'Student'))

class UserProfileForm(forms.ModelForm):
    occupation = forms.ChoiceField(choices=OCCUPATION)
    class Meta:
        model = UserProfile
        fields = ['picture', 'age', 'occupation', 'university', 'company']

# https://stackoverflow.com/questions/13482753/use-field-label-as-placeholder-in-django-crispy-forms
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        helper = self.helper = FormHelper()

        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            helper.form_show_labels = False
            field.widget.attrs['placeholder'] = field.label

# The form is for user to edit their email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

# The form is for user to edit their profile
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'age', 'occupation', 'university', 'company']
