from django.urls import path

from user.views import Signup, Signin, Logout, Profile


urlpatterns = [
    path('signup/', Signup, name='signup'),
    path('sigin/', Signin, name='signin'),
    path('logout/', Logout, name='logout'),
    path('profile/', Profile, name='profile'),
]