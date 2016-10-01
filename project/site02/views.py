from django.shortcuts import render,redirect
from forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from models import UserExtended


def home(request):
    # if user_registered(request):
    #     message = "Welcome, "
    # elif request.session.has_key("Site2_user"):
    #     message = "Welcome Back, "
    # else:
    #     return redirect("/signup2/")
    # message += request.session["email"]
    message = "Under Construction. . . Please be Patient and come back later. ."
    # return render(request, "site02/home.html", {'message': message})
    return render(request, "site02/home.html", {'message': message})


def user_registered(request):
    if "hashed_email" in request.COOKIES:
        email = request.COOKIES['hashed_email']
        hashed_emails = UserExtended.objects.values('hashed_email')
        if email in hashed_emails:
            user = User.objects.get(hashed_email=email)
            login(request, user)
            request.session["Site1_user_verified"] = True
            request.session["email"] = email
            return True
    return False


def signup(request):
    if request.method == "GET":
        form = SignupForm()
        return render(request, "site02/signup.html", {'form':form})
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data["name"]
            email = data["email"]
            password = data["password"]
            user = User.objects.create_user(first_name=name, email=email, password=password)
            user.save()
            request.session["username"] = email
            request.session["Site2_user"] = True
            return redirect("/login2/")
        else:
            form = SignupForm(request.POST)
            return render(request, "site02/signup.html", {'form': form})


def login2(request):
    if request.method == "GET":
        return render(request,"site02/login.html")
    else:
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)
        if user:
            request.session["username"] = email
            request.session["Site2_user"] = True
            login(request, user)
            return redirect("/site2/")
        else:
            return render(request, "site02/login.html",{'message':"Enter correct details"})



