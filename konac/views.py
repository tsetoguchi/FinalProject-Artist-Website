from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms
from django.urls import reverse
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.

def index(request):

    # scope = 'user-top-read'
    # username = 'konac'

    # token = util.prompt_for_user_token(username, scope)


    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = UserCreationForm(request.POST)

        # Create a form instance and populate it with data from the request (binding):
        email = (request.POST["email"])
        password = (request.POST["password"])

        try:
            user = User.objects.get(username=email)
            return render(request, "konac/error.html", {"message": "Email already exists!"})
        except User.DoesNotExist:
            user = User.objects.create_user(username=email, password=password)
            return render(request, "konac/index.html")

    # if user is logged in, redirect to index2
    if ('loggedin' in request.session) and (request.session['loggedin'] is True):
            return render(request, "konac/index2.html")

    # If GET request, return index
    return render(request, "konac/index.html")

def index2(request):

        # If this is a POST request then process the Form data
        if request.method == 'POST':

            # Create a form instance and populate it with data from the request (binding):
            form = UserCreationForm(request.POST)

            # Create a form instance and populate it with data from the request (binding):
            email = (request.POST["email"])
            password = (request.POST["password"])
            print('got user and pass')

            # Authenticate user
            user = authenticate(username = email, password = password)
            if user is not None:
                request.session['loggedin'] = True
                request.session['username'] = email
            else:
                return render(request, "konac/error.html", {"message": "Invalid E-mail or Password!"})

        if ('loggedin' in request.session) and (request.session['loggedin'] is True):
            return render(request, "konac/index2.html")

        if request.method == 'GET':
            return render(request, "konac/index.html")

def music(request):

    # if user is logged in, redirect to music2
    if ('loggedin' in request.session) and (request.session['loggedin'] is True):
        print(request.session['username'])
        return render(request, "konac/music2.html")

    return render(request, "konac/music.html")

def terms(request):
    return render(request, "konac/terms.html")

def logout(request):

    # if user is logged in, redirect to music2
    if ('loggedin' in request.session) and (request.session['loggedin'] is True):
        request.session['loggedin'] = False
        request.session['username'] = None
        return render(request, "konac/logout.html")

    # else render index
    return render(request, "konac/index.html")

def comments(request):
    return render(request, "konac/comments.html")
