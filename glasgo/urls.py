from django.urls import path
from glasgo import views

app_name = 'glasgo'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/contact-us/', views.contact, name='contact'),
    path('login/', views.log_in, name='login'),
    path('login/register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('user/<slug:user_profile_slug>/', views.show_user_profile, name='show_user_profile'),
    path('user/<slug:user_profile_slug>/edit/', views.edit_profile, name='edit_profile'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('post/<slug:post_slug>/', views.show_post, name='show_post'),

]
