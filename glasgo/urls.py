from django.urls import path
from glasgo import views

app_name = 'glasgo'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.log_in, name='login'),
    path('login/register/', views.register, name='register')
]
