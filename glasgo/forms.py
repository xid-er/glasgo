from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
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
