from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms
from django.urls import reverse
from .models import Comments
import json, os, requests, webbrowser

# Comment Sections

commentSectionflt = {
        }

commentSectionwlg = {
        }

commentSectionaway = {
        }

commentSectionhome = {
        }

# Create your views here.

def index(request):

    # Submit a GET request to Youtube API
    res = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UUzAjvFPO5L8aEdHbb8DafeQ&key=AIzaSyDANFYwuTNW2FnqzK8ogc-QlRVB9EHy7G0')

    # Check if request was successful
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')

    # Convert response to JSON
    json_data = json.dumps(res.json(), indent=4, separators=(',', ': '))

    # Parse response to python dictionary
    parsed = json.loads(f'{json_data}')

    # Get title and youtube video ID of newest release
    title = str(parsed['items'][0]['snippet']['title'])
    id = str(parsed['items'][0]['snippet']['resourceId']['videoId'])
    videoURL = (f'https://www.youtube.com/embed/{id}')
    context = {
        'title': title,
        'videoURL': videoURL
    }

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

            # Submit a GET request to Youtube API
            res = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UUzAjvFPO5L8aEdHbb8DafeQ&key=AIzaSyDANFYwuTNW2FnqzK8ogc-QlRVB9EHy7G0')

            # Check if request was successful
            if res.status_code != 200:
                raise Exception('ERROR: API request unsuccessful.')

            # Convert response to JSON
            json_data = json.dumps(res.json(), indent=4, separators=(',', ': '))

            # Parse response to python dictionary
            parsed = json.loads(f'{json_data}')

            # Get title and youtube video ID of newest release
            title = str(parsed['items'][0]['snippet']['title'])
            id = str(parsed['items'][0]['snippet']['resourceId']['videoId'])
            videoURL = (f'https://www.youtube.com/embed/{id}')
            context = {
                'title': title,
                'videoURL': videoURL
            }
            return render(request, "konac/index.html", context)

    # if user is logged in, redirect to index2
    if ('loggedin' in request.session) and (request.session['loggedin'] is True):
            return render(request, "konac/index2.html")

    # If GET request, return index
    return render(request, "konac/index.html", context)

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

             # Submit a GET request to Youtube API
            res = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UUzAjvFPO5L8aEdHbb8DafeQ&key=AIzaSyDANFYwuTNW2FnqzK8ogc-QlRVB9EHy7G0')

            # Check if request was successful
            if res.status_code != 200:
                raise Exception('ERROR: API request unsuccessful.')

            # Convert response to JSON
            json_data = json.dumps(res.json(), indent=4, separators=(',', ': '))

            # Parse response to python dictionary
            parsed = json.loads(f'{json_data}')

            # Get title and youtube video ID of newest release
            title = str(parsed['items'][0]['snippet']['title'])
            id = str(parsed['items'][0]['snippet']['resourceId']['videoId'])
            videoURL = (f'https://www.youtube.com/embed/{id}')
            context = {
                'title': title,
                'videoURL': videoURL
            }
            return render(request, "konac/index2.html", context)

        if request.method == 'GET':

             # Submit a GET request to Youtube API
            res = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UUzAjvFPO5L8aEdHbb8DafeQ&key=AIzaSyDANFYwuTNW2FnqzK8ogc-QlRVB9EHy7G0')

            # Check if request was successful
            if res.status_code != 200:
                raise Exception('ERROR: API request unsuccessful.')

            # Convert response to JSON
            json_data = json.dumps(res.json(), indent=4, separators=(',', ': '))

            # Parse response to python dictionary
            parsed = json.loads(f'{json_data}')

            # Get title and youtube video ID of newest release
            title = str(parsed['items'][0]['snippet']['title'])
            id = str(parsed['items'][0]['snippet']['resourceId']['videoId'])
            videoURL = (f'https://www.youtube.com/embed/{id}')
            context = {
                'title': title,
                'videoURL': videoURL
            }
            return render(request, "konac/index.html", context)

def music(request):

    # if user is logged in, redirect to music2
    if ('loggedin' in request.session) and (request.session['loggedin'] is True):
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

    # if user is logged in, redirect to music2
    if ('loggedin' in request.session) and (request.session['loggedin'] is True):

     # If this is a POST request then process the Form data
        if request.method == 'POST':

            # Create a form instance and populate it with data from the request (binding):
            form = UserCreationForm(request.POST)

            # Create a form instance and populate it with data from the request (binding):
            comment = (request.POST["comment"])
            user = request.session['username']

            # Comment formatted
            packagedComment = (f"{user}: {comment}")

            # if lastComment is identical to posted comment, do not add to comment section
            if (packagedComment) == (request.session['lastComment']):
                    context = {
                        'comments': commentSectionflt
                    }
                    return render(request, "konac/flutter.html", context)

            # Save previous comment
            request.session['lastComment'] = packagedComment

            # Check if user has made a comment before
            if user in commentSectionflt:
                commentSectionflt[user].append(packagedComment)

            # If the user does not exist, create a new key value pair in dict comment section
            else:
                commentSectionflt[user] = []
                commentSectionflt[user].append(packagedComment)
                context = {
                    'comments': commentSectionflt
                }
                return render(request, "konac/flutter.html", context)

        if request.method =='GET':
            user = request.session['username']
            context = {
                'comments': commentSectionflt
            }
            return render(request, "konac/flutter.html", context)


        context = {
                'comments': commentSectionflt
            }
        return render(request, "konac/flutter.html", context)

    # If user is not logged in
    else:
        context = {
                'comments': commentSectionflt
            }
        return render(request, "konac/index.html", context)

def wontletgo(request):

    # if user is logged in, redirect to music2
    if ('loggedin' in request.session) and (request.session['loggedin'] is True):

     # If this is a POST request then process the Form data
        if request.method == 'POST':

            # Create a form instance and populate it with data from the request (binding):
            form = UserCreationForm(request.POST)

            # Create a form instance and populate it with data from the request (binding):
            comment = (request.POST["comment"])
            user = request.session['username']

            # Comment formatted
            packagedComment = (f"{user}: {comment}")

            # if lastComment is identical to posted comment, do not add to comment section
            if (packagedComment) == (request.session['lastComment']):
                    context = {
                        'comments': commentSectionwlg
                    }
                    return render(request, "konac/wontletgo.html", context)

            # Save previous comment
            request.session['lastComment'] = packagedComment

            # Check if user has made a comment before
            if user in commentSectionwlg:
                commentSectionwlg[user].append(packagedComment)

            # If the user does not exist, create a new key value pair in dict comment section
            else:
                commentSectionwlg[user] = []
                commentSectionwlg[user].append(packagedComment)
                context = {
                    'comments': commentSectionwlg
                }
                return render(request, "konac/wontletgo.html", context)

        if request.method =='GET':
            user = request.session['username']
            context = {
                'comments': commentSectionwlg
            }
            return render(request, "konac/wontletgo.html", context)


        context = {
                'comments': commentSectionwlg
            }
        return render(request, "konac/wontletgo.html", context)

    # If user is not logged in
    else:
        context = {
                'comments': commentSectionwlg
            }
        return render(request, "konac/index.html", context)

def away(request):

    # if user is logged in, redirect to music2
    if ('loggedin' in request.session) and (request.session['loggedin'] is True):

     # If this is a POST request then process the Form data
        if request.method == 'POST':

            # Create a form instance and populate it with data from the request (binding):
            form = UserCreationForm(request.POST)

            # Create a form instance and populate it with data from the request (binding):
            comment = (request.POST["comment"])
            user = request.session['username']

            # Comment formatted
            packagedComment = (f"{user}: {comment}")

            # if lastComment is identical to posted comment, do not add to comment section
            if (packagedComment) == (request.session['lastComment']):
                    context = {
                        'comments': commentSectionaway
                    }
                    return render(request, "konac/away.html", context)

            # Save previous comment
            request.session['lastComment'] = packagedComment

            # Check if user has made a comment before
            if user in commentSectionaway:
                commentSectionaway[user].append(packagedComment)

            # If the user does not exist, create a new key value pair in dict comment section
            else:
                commentSectionaway[user] = []
                commentSectionaway[user].append(packagedComment)
                context = {
                    'comments': commentSectionaway
                }
                return render(request, "konac/away.html", context)

        if request.method =='GET':
            user = request.session['username']
            context = {
                'comments': commentSectionaway
            }
            return render(request, "konac/away.html", context)


        context = {
                'comments': commentSectionaway
            }
        return render(request, "konac/away.html", context)

    # If user is not logged in
    else:
        context = {
                'comments': commentSectionaway
            }
        return render(request, "konac/index.html", context)

def home(request):

    # if user is logged in, redirect to music2
    if ('loggedin' in request.session) and (request.session['loggedin'] is True):

     # If this is a POST request then process the Form data
        if request.method == 'POST':

            # Create a form instance and populate it with data from the request (binding):
            form = UserCreationForm(request.POST)

            # Create a form instance and populate it with data from the request (binding):
            comment = (request.POST["comment"])
            user = request.session['username']

            # Comment formatted
            packagedComment = (f"{user}: {comment}")

            # if lastComment is identical to posted comment, do not add to comment section
            if (packagedComment) == (request.session['lastComment']):
                    context = {
                        'comments': commentSectionhome
                    }
                    return render(request, "konac/home.html", context)

            # Save previous comment
            request.session['lastComment'] = packagedComment

            # Check if user has made a comment before
            if user in commentSectionhome:
                commentSectionhome[user].append(packagedComment)

            # If the user does not exist, create a new key value pair in dict comment section
            else:
                commentSectionhome[user] = []
                commentSectionhome[user].append(packagedComment)
                context = {
                    'comments': commentSectionhome
                }
                return render(request, "konac/home.html", context)

        if request.method =='GET':
            user = request.session['username']
            context = {
                'comments': commentSectionhome
            }
            return render(request, "konac/home.html", context)


        context = {
                'comments': commentSectionhome
            }
        return render(request, "konac/home.html", context)

    # If user is not logged in
    else:
        context = {
                'comments': commentSectionhome
            }
        return render(request, "konac/index.html", context)