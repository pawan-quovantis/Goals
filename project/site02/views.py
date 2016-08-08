from django.shortcuts import render,redirect
from forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


@login_required(login_url='login1')
def home(request):
    name = request.session["username"]
    return render(request, "site02/home.html", {'name':name})


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
            # request.session["username"] = name
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
            login(request, user)
            return redirect("/site2/")
        else:
            return render(request, "site02/login.html",{'message':"Enter correct details"})



