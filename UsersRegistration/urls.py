from django.urls import path, include
from UsersRegistration import views

urlpatterns = [
    path('get_user_register', views.get_user_register, name='get_user_register'),
]
