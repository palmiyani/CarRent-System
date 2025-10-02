from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

from app1.models import Car
# Create your views here.


def index(request):
    return render(request,'index.html')


def services(request):
    return render(request,'services.html')


def cars(request):
    c1 = Car.objects.all()
    return render(request,'cars.html',{'c1':c1})


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def logindemo(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,"Bad Credentials")
            return redirect('/logindemo/')
    return render(request, 'login.html')



def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.firstname = fname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('/login/')
    return render(request, 'registration.html')


def Logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('/')


def car(request):
    if request.method=="POST":
        user = request.POST['user']
        car_name = request.POST['car_name']
        price = request.POST['price']
        company = request.POST['company']
        location = request.POST['location']
        seat = request.POST['seat']
        transmission = request.POST['transmission']
        car_img = request.Files['car_img']


        s = Car.objects.create(user=user,car_name=car_name,price=price,company=company,location=location,seat=seat,transmission=transmission,image=car_img,)

        return HttpResponse('<h1>Data is inserted.</h1>')

    return render(request,'')