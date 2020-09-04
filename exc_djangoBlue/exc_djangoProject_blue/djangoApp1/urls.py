from django.urls import path
from djangoApp1 import views

app_name = 'djangoApp1'

urlpatterns = [
    path('tutors/', views.tutorsPage, name='tutorsPage'),
    path('registration/', views.registrationPage, name='registrationPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutPage, name='logoutPage'),
    path('main/', views.mainPage, name='mainPage'),
]