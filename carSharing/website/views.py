from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as auth_login
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def signup(request):
    context = {}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            '''raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)'''

            messages.success(request, "Your account has been created successfully!")
            return redirect('login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'signup.html', context)

def login(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("/")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            messages.success(request, "You are logged in successfully!")

            if user:
                auth_login(request, user)
                return redirect("index")

    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'login.html', context)

def signout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def publishRide(request):

    if(request.method == "POST"):
        user = request.user
        pickup = request.POST.get('pickup')
        drop = request.POST.get('drop')
        date = request.POST.get('date')
        time = request.POST.get('time')
        seats = request.POST.get('seats')
        price = request.POST.get('price')
        phone = request.POST.get('phone')
        
        ride = PublishRide(user=user, pickup=pickup, drop=drop, date=date, time=time, seats=seats, price=price, phone=phone)
        ride.save()

        return redirect('/')

    return render(request, "publishRide.html")

def search(request):

    # s = PublishRide.objects.all().order_by('date')
    pickup_search = PublishRide.objects.values_list('pickup', flat=True).distinct()
    drop_search = PublishRide.objects.values_list('drop', flat=True).distinct()
    date_search = PublishRide.objects.values_list('date', flat=True).distinct()
    pickup = request.GET.get('pickup')
    drop = request.GET.get('drop')
    date = request.GET.get('date')
    rides = PublishRide.objects.filter(pickup=pickup, drop=drop, date=date)

    if 'pickup' in request.GET:
        pickup = request.GET['pickup']
        if pickup:
            rides = rides.filter(pickup=pickup)

    if 'drop' in request.GET:
        drop = request.GET['drop']
        if drop:
            rides = rides.filter(drop=drop)

    if 'date' in request.GET:
        date = request.GET['date']
        if date:
            rides = rides.filter(date=date)

    data = {
        'rides': rides,
        'pickup_search': pickup_search,
        'drop_search': drop_search,
        'date_search': date_search,
    }

    return render(request, "search.html", data)

@login_required(login_url='login')
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }

    return render(request, 'profile.html', context)
