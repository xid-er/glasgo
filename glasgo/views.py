from django.shortcuts import render
from django.http import HttpResponse
from glasgo.forms import UserForm, UserProfileForm

def index(request):
    return HttpResponse("Rango says hey there partner!\n<a href='/glasgo/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page.")

def log_in(request):
    return render(request, 'glasgo/login.html')

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
