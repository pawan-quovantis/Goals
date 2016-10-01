from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from models import *
from forms import *
import hashlib


def signup(request):
    if request.method == "GET":
        return render(request, 'site01/signup.html')
    else:
        name = request.POST["name"]
        # phone = request.POST["phone"]
        email = request.POST["email"]
        password = request.POST["password"]
        # date_of_birth = request.POST["dob"]
        User.objects.create_user(first_name=name, username=email, password=password,
                                 date_joined=datetime.datetime.now())
        return create_session_and_response(request, email, password)


def login1(request):

    if request.user.is_authenticated():
        return redirect('/')
    if request.method == "GET":
        return render(request, "site01/login.html")
    else:
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)
        if user:
            return create_session_and_response(request, email, password)
        else:
            return render(request, "site01/login.html", {'message': "Enter correct details", 'user': request.user})


def create_session_and_response(request, email, password):
    create_session(request, email, password)
    response = redirect('/')
    response.set_cookie('hashed_email', str(hashlib.sha256(email).hexdigest()))
    return response


def create_session(request, email, password):
    request.session["username"] = email
    request.session["loggedin"] = True
    user = authenticate(username=email, password=password)
    login(request, user)


@login_required(login_url='/login/')
def home(request):
    if request.user.is_authenticated():
        email = request.session["username"]
        return render(request, "site01/home.html", {'email': email})
    else:
        return redirect('/login/')


@login_required(login_url='/login/')
def logout1(request):
    if request.method == "GET":
        return render(request, 'site01/logout.html', {'user': request.user})
    else:
        logout(request)
        response = redirect('/')
        response.delete_cookie("user")
        request.session["loggedin"] = False
        return response


def user_can_insert(user):
    if user.is_authenticated() and user.has_perm('site01.add_author'):
        return True
    else:
        return False


@login_required(login_url='/login/')
def display_books(request):
    if request.method == "GET":
        books = Book.objects.all()
        if books:
            return render(request, "site01/display_books.html", {"books": books})
        else:
            message = "No Books to display, Please go ahead and add some."
            link = "/insert_books/"
            return render(request, "site01/display_books.html", {"message": message, "link": link})


@login_required(login_url='/login/')
def insert_books(request):
    if request.method == "GET":
        book_form = BookForm()
        return render(request, "site01/insert_books.html", {"book_form": book_form})
    else:
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            data = book_form.cleaned_data
            title = data["title"]
            author = data["author"]
            author = author.split()[0]
            publisher = data["publisher"]
            publishing_date = data["publishing_date"]
            author_object = Author.objects.all().filter(first_name=author).first()
            publisher_object = Publisher.objects.all().filter(name=publisher).first()
            if author_object is None:
                message = "Author does not exist in out database, wanna add first?"
                link = "/insert_authors/"
                return render(request, "site01/insert_books.html", {"book_form": book_form, "message": message,
                                                                    "link": link, "entity": "Author",
                                                                    'user': request.user})
            if publisher_object is None:
                message = "Publisher does not exist in out database, wanna add first?"
                link = "/insert_publisher/"
                return render(request, "site01/insert_books.html", {"book_form": book_form, "message": message,
                                                                    "link": link, "entity": "Publisher",
                                                                    'user': request.user})
            try:
                book = Book(title=title, publication_date=publishing_date, publisher=publisher_object)
                book.save()
                book.authors.add(author_object)
                book.save()
                return redirect('/display_books/')
            except Exception, e:
                error = str(e)
                return render(request, "site01/insert_books.html", {"book_form": book_form, "error": error})
        else:
            errors = book_form.errors
            return render(request, "site01/insert_books.html", {"book_form": book_form, "errors": errors})


@login_required(login_url='/login/')
def display_authors(request):
    if request.method == "GET":
        authors = Author.objects.all()
        if authors:
            return render(request, "site01/display_authors.html", {"authors": authors})
        else:
            message = "No Authors to display, Please go ahead and add some."
            link = "/insert_authors/"
            return render(request, "site01/display_authors.html", {"message": message, "link": link})


@login_required(login_url='/login/')
def insert_authors(request):
    if request.method == "GET":
        author_form = AuthorForm()
        return render(request, "site01/insert_authors.html", {"author_form": author_form})
    else:
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            data = author_form.cleaned_data
            first_name = data["first_name"]
            last_name = data["last_name"]
            email = data["email"]
            try:
                author = Author(first_name=first_name, last_name=last_name, email=email)
                author.save()
                return redirect("/display_authors/")
            except Exception, e:
                error = str(e)
                return render(request, "site01/insert_books.html", {"author_form": author_form, "error": error})

        else:
            errors = author_form.errors
            return render(request, "site01/insert_books.html", {"author_form": author_form, "errors": errors})


@login_required(login_url='/login/')
def display_publishers(request):
    if request.method == "GET":
        publishers = Publisher.objects.all()
        if publishers:
            return render(request, "site01/display_publishers.html", {"publishers": publishers})
        else:
            message = "No Publishers to display, Please go ahead and add some."
            link = "/insert_publishers/"
            return render(request, "site01/display_publishers.html", {"message": message, "link": link})


@login_required(login_url='/login/')
@user_passes_test(user_can_insert, redirect_field_name='/display_publishers/')
def insert_publishers(request):
    if request.method == "GET":
        publisher_form = PublisherForm()
        return render(request, "site01/insert_publishers.html", {"publisher_form": publisher_form})
    else:
        publisher_form = PublisherForm(request.POST)
        if publisher_form.is_valid():
            data = publisher_form.cleaned_data
            name = data["name"]
            address = data["address"]
            city = data["city"]
            state = data["state"]
            country = data["country"]
            website = data["website"]
            try:
                publisher = Publisher(name=name, address=address, city=city, state_province=state, country=country,
                                      website=website)
                publisher.save()
                return redirect("/display_publishers/")
            except Exception, e:
                error = str(e)
                return render(request, "site01/insert_publishers.html", {"publisher_form": publisher_form,
                                                                         "error": error})

        else:
            errors = publisher_form.errors
            return render(request, "site01/insert_publishers.html", {"publisher_form": publisher_form,
                                                                     "errors": errors})
