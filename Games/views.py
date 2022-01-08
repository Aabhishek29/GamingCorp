from django.shortcuts import render
from UsersRegistration.forms import UserRegistrationForm
from Support.forms import UsersFeedBack


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    forms = UserRegistrationForm()
    return render(request, 'signUp.html', {'form': forms})


def AboutUs(request):
    return render(request, 'aboutUs.html')


def ContactUs(request):
    forms = UsersFeedBack()
    return render(request, 'contactUs.html', {'form': forms})
