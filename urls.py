from django.urls import path
from account import views

urlpatterns = [
    path('singup/',views.UserRegisterView,name='singup'),
    path('singin/',views.UserLoginView,name='singin'),
    path('profile/',views.UserProfile,name='profile'),
    path('logout/',views.UserLogout,name='logout'),
    path('change-password/',views.UserPasswordChange,name='change_password'),
    path('update-profile/',views.UserProfileEdit,name='update_profile'),
]
