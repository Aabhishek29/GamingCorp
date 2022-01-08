from django.urls import path, include
from Games import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.register, name='signup'),
    path('aboutUs', views.AboutUs, name='aboutUs'),
    path('contactUs', views.ContactUs, name='contactUs')
]