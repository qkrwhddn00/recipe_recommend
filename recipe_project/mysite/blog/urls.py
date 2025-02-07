from django.urls import path
from blog.views import home_view, main_view, signup_view

urlpatterns = [
    path('',home_view ,name='home'),
    path('main/',main_view, name='main'),
    path('singup/',signup_view, name='signup'),
]