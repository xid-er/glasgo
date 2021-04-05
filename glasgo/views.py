from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import View

from glasgo.forms import UserForm, UserProfileForm, PostForm, CommentForm
from glasgo.models import UserProfile, Post, Comment, Like, Favourite

def index(request):
    context_dict = {}
    recent_post_list = Post.objects.order_by('-post_date_time')
    top_post_list = Post.objects.order_by('-likes')
    context_dict['recent'] = recent_post_list
    context_dict['top'] = top_post_list
    return render(request, 'glasgo/index.html', context=context_dict)

def about(request):
    return render(request, 'glasgo/about.html')

def contact(request):
    return render(request, 'glasgo/contact_us.html')

@login_required
def show_user_profile(request, user_name):
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        return None

    context_dict = {}

    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    top_posts = Post.objects.filter(user_name=user_name).order_by('-likes')
    recent_posts = Post.objects.filter(user_name=user_name).order_by('-post_date_time')
    favourite_posts = Post.objects.filter(user_name=user_name).order_by('-post_date_time')
    context_dict['user_profile'] = user_profile
    context_dict['selected_user'] = user
    context_dict['recent'] = recent_posts
    context_dict['top'] = top_posts
    context_dict['favourites'] = favourite_posts

    return render(request, 'glasgo/profile.html', context=context_dict)

@login_required
def edit_profile(request, user_name):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=rquest.user.profile)
        if user_form.is_Valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('my_profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.profile)
    context = {'user_form': user_form, 'profile_form': profile_form, }

    return render(request,'glasgo/edit_profile.html', context)

# https://towardsdatascience.com/build-a-social-media-website-with-django-feed-app-backend-part-4-d82facfa7b3
@login_required
def add_post(request):
    user = request.user
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        post_form.user_name = request.user
        if post_form.is_valid():
            # breakpoint()
            data = post_form.save()
            data.user_name = user
            data.save(commit=True)
            messages.success(request, f'Posted Successfully')
            return redirect(reverse('glasgo/index.html'))
        else:
            print(post_form.errors)
    else:
        post_form = PostForm()
    return render(request, 'glasgo/add_post.html', {'post_form':post_form})

def show_post(request, post_number):
    context_dict = {}
    try:
        post = Post.objects.get(post_number=post_number)
        user = request.user
        is_liked = Like.objects.filter(user=user, post=post)
        is_favourite = Favourite.objects.filter(user=user, post=post)
        post_type = post.post_type

        if request.method == 'POST':
            form = CommentForm(request.POST)
            data = form.save(commit=False)
            data.post = post
            data.username = user
            data.save()
        else:
            form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-comment_date_time')
        context_dict['comments'] = comments
        context_dict['form'] = form
        context_dict['is_liked'] = is_liked
        context_dict['is_favourite'] = is_favourite
        context_dict['post_type'] = post_type
    except Post.DoesNotExist:
        return render(request, 'glasgo/')

    return render(request, 'glasgo/view_post.html', context=context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('glasgo:index'))
            else:
                return HttpResponse("Your GlasGO account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'glasgo/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('glasgo:index'))

def register(request):
    # A boolean value to tell the template
    # whether the registration was successful.
    # if the registration succeeds, the value will change to true
    registered = False

    # If it's a HTTP POST, we're interested in processing from data.
    if request.method == 'POST':
        # to grab information from the raw form information.
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # if the two forms are both valid,
        # then save the user's form data to the database.
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user


            # check whether the user provide a profile photo?
            # if yes, get it from the input form and put it in the UserProfile
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # save the UserProfile model instance.
            profile.save()
            # change it to be true, since the registration was successful.
            registered = True
        else:

            # print the problem - mistakes or something wrong
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, then we render our form using two ModelForm instances
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'glasgo/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})

class LikePostView(View):
    @method_decorator(login_required)
    def get(self, request):
        post_number = request.GET['post_number']
        try:
            post = Post.objects.get(post_number=int(post_number))
        except Post.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        post.post_likes = post.post_likes + 1
        post.save()

        return HttpResponse(post.post_likes)

class FavoritePostView(View):
    def get(self, request):
        post_number = request.GET['post_number']
        try:
            post = Post.objects.get(post_number=int(post_number))
            if post.is_favorite:
                post.is_favorite = False
            else:
                post.is_favorite = True
        except Post.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        post.save()

        return HttpResponse(post.is_favorite)
