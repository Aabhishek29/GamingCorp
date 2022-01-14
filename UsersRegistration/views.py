from django.shortcuts import render
from .models import Users
from django.http import HttpResponseRedirect
from django.contrib import messages
import datetime
# Create your views here.


def get_user_register(request):
    if request.method == 'POST':
        print("Working")
        username = request.POST['name']
        phnumber = request.POST['phNumber']
        email = request.POST['Email']
        pswd = request.POST['password']
        createdAt = datetime.date.today()
        try:
            data = Users(username, phnumber, email, pswd, createdAt)
            data.save()
            print("Working2")
        except Exception:
            print(Exception)
        return HttpResponseRedirect('/')
    return render(request, 'index.html')
