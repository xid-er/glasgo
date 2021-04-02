from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from glasgo.models import UserProfile, Post, Comment

from glasgo.forms import UserForm, UserProfileForm, PostForm, CommentForm

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

def show_user_profile(request, user_profile_slug):
    # TODO get list of favorites once models updated
    context_dict = {}
    top_posts = Post.objects.filter(user_name=user_profile_slug).order_by('-likes')
    recent_posts = Post.objects.filter(user_name=user_profile_slug).order_by('-post_date_time')
    context_dict['recent'] = recent_posts
    context_dict['top'] = top_posts

    return render(request, 'glasgo/profile.html', context=context_dict)

@login_required
def edit_profile(request, user_profile_slug):
    # TODO think about how to implement this
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


@login_required
def add_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('glasgo/index.html'))
        else:
            print(form.errors)
    else:
        return render(request, 'glasgo/add_post.html', {'form': form})

def show_post(request, post_slug):
    context_dict = {}
    try:
        post = Post.objects.get(slug=post_slug)
        comments = Comment.objects.filter(post=post).order_by('-comment_date_time')
        context_dict['post'] = post
        context_dict['comments'] = comments
    except Post.DoesNotExist:
        context_dict['post'] = None
        context_dict['comments'] = None

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
