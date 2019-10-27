from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('meetups', views.meet_ups, name='meet_ups'),
    path('profile', views.profile, name='profile')

]