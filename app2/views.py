from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from app2.models import Application
from app1.models import Car
# Create your views here.


def index1(request):
    return render(request,'index1.html')


def services1(request):
    return render(request,'services1.html')


def cars1(request):
    c1 = Car.objects.all()
    return render(request, 'cars1.html', {'c1': c1})


def about1(request):
    return render(request,'about1.html')


def contact1(request):
    return render(request,'contact1.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('/user_site/cars1')
        else:
            messages.error(request,"Bad Credentials")
            return redirect('/user_site/login1')
    return render(request, 'login1.html')



def registration1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.firstname = fname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('/user_site/login1/')
    return render(request, 'registration1.html')


def Logout1(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('/')


def application(request):
    if request.method=="POST":
        first_name =request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        driver_license_number = request.POST['driver_license_number']
        pickup_location = request.POST['pickup_location']
        drop_location = request.POST['drop_location']
        pickup_date = request.POST['pickup_date']
        pickup_time = request.POST['pickup_time']
        return_date = request.POST['return_date']
        return_time = request.POST['return_time']

        s = Application.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_number=mobile_number,
            driver_license_number=driver_license_number,
            pickup_location=pickup_location,
            drop_location=drop_location,
            pickup_date=pickup_date,
            pickup_time=pickup_time,
            return_date=return_date,
            return_time=return_time,
        )

        return HttpResponse('<h1>Data is inserted.</h1>')

    return render(request, 'application.html')
