from django.urls import path
from glasgo import views

app_name = 'glasgo'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/contact-us/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('login/register/', views.register, name='register'),
    path('user/<slug:user_profile_slug>/', views.show_user_profile, name='show_user_profile'),
    path('user/<slug:user_profile_slug>/edit/', views.edit_profile, name='edit_profile'),
    path('add_post/', views.add_post, name='add_post'),
    path('post/<post_number>/', views.show_post, name='show_post'),

]
