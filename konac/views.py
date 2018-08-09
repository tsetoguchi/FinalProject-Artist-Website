from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms
from django.urls import reverse
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from .models import Comments

# Comment Section
commentSection = {
        }

# Create your views here.

def index(request):

    scope = 'user-library-read'

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)



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

def flutter(request):

 # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = UserCreationForm(request.POST)

        # Create a form instance and populate it with data from the request (binding):
        comment = (request.POST["comment"])
        user = request.session['username']

        # Comment formatted
        packagedComment = (f"{user}: {comment}")

        # if lastComment is identical to posted comment, do not add to list
        if (packagedComment) == (request.session['lastComment']):
                context = {
                    'comments': commentSection[user]
                }
                return render(request, "konac/flutter.html", context)


        # Save previous comment
        request.session['lastComment'] = packagedComment


        # Check if user has made a comment before
        if user in commentSection.keys():
            commentSection[user].append(packagedComment)

        # If the user does not exist, create a new key value pair in dict commentSection
        else:
            commentSection[user] = []
            commentSection[user].append(packagedComment)

        context = {
            'comments': commentSection[user]
        }
        return render(request, "konac/flutter.html", context)

    if request.method =='GET':
        user = request.session['username']
        if user in commentSection.keys():

            context = {
                'comments': commentSection[user]
            }
            # request.session['lastComment'] = None
            return render(request, "konac/flutter.html", context)

        return render(request, "konac/flutter.html")

    print(commentSection[user])
    context = {
            'comments': commentSection[user]
        }
    return render(request, "konac/flutter.html", context)
