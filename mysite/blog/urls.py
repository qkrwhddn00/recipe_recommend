from django.urls import path
from blog.views import home_view, main_view, signup_view, koreanfood, korean_food_list

urlpatterns = [
    path('',home_view ,name='home'),
    path('main/',main_view, name='main'),
    path('singup/',signup_view, name='signup'),
    path('koreanfood/',koreanfood, name='koreanfood'),
    path('korean-food/', korean_food_list, name='korean_food_list'),
]