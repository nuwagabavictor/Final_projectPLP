from django.shortcuts import render, get_object_or_404, redirect
import json
import urllib.request
import urllib.parse
from .forms import SongForm, AlbumForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .models import Artist, Album, Song, user, song_instance
#homepage
def home(request):
    return render(request, 'mysport/home.html')
#view artists
def index(request):
    artists = Artist.objects.all().values()
    num_artists = Artist.objects.all().count()
    context = {
        'artists': artists,
        'num_artists': num_artists,
    }
    return render(request, 'mysport/artist.html', context)

def add(request):
    return render(request, 'mysport/add_artist.html')

 #view added artist 
def view(request):
  artists = Artist.objects.all().values()
  context = {
    'artists': artists,
  }
  return render(request, 'mysport/index.html', context)

  
#add artist
def addartist_record(request):
    if request.method == 'POST':
        x = request.POST['Name']
        y = request.POST['bio']
        mysport = Artist(Name=x, bio=y)
        mysport.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'mysport/add_artist.html')

#delete song, artist, album
MODEL_MAP = {
    'artist': Artist,
    'album': Album,
    'song': Song
}

def delete_object(request, model_type, id):
    model = MODEL_MAP.get(model_type)
    if model is None:
        return redirect('home')
    object = get_object_or_404(model, id=id)
    object.delete()
    
    if model_type == 'artist':
        return redirect('index')  
    elif model_type == 'album':
        return redirect('album')  
    elif model_type == 'song':
        return redirect('music')  

# def delete(request, id):
#     artist = get_object_or_404(Artist, id=id)
#     artist.delete()
#     return redirect('index')


#render update form
def update_a(request, id):
    myartist = get_object_or_404(Artist, id=id)
    context = {
        'myartist': myartist,
    }
    return render(request, 'mysport/update_artist.html', context)

#render update form
def update_s(request, id):
    myalbum = get_object_or_404(Album, id=id)
    context = {
        'myalbum': myalbum,
    }
    return render(request, 'mysport/update_album.html', context)

#render update form
def update_a(request, id):
    mysong = get_object_or_404(Song, id=id)
    context = {
        'mysong': mysong,
    }
    return render(request, 'mysport/update_song.html', context)

# def updaterecord_artist(request, id):
#     if request.method == 'POST':
#         Name = request.POST['Name']
#         bio = request.POST['bio']
#         myartist = get_object_or_404(Artist, id=id)
#         myartist.Name = Name
#         myartist.bio = bio
#         myartist.save()
#         return HttpResponseRedirect(reverse('index'))
#update artist
def update_artist(request, id):
    myartist = get_object_or_404(Artist, id=id)

    if request.method == 'POST':
        myartist.Name = request.POST['Name']
        myartist.bio = request.POST['bio']
        myartist.save()
        return HttpResponseRedirect(reverse('index'))

    context = {
        'myartist': myartist,
    }
    return render(request, 'mysport/update_artist.html', context)

# Update Song View
def update_song(request, id):
    mysong = get_object_or_404(Song, id=id)

    if request.method == 'POST':
        mysong.title = request.POST['title']
        mysong.artist = request.POST['artist']
        mysong.album = request.POST['album']
        mysong.duration = request.POST['duration']
        mysong.release_date = request.POST['release_date']
        mysong.save()
        return HttpResponseRedirect(reverse('music'))  # Redirect to the songs index

    context = {
        'mysong': mysong,
    }
    return render(request, 'mysport/update_song.html', context)

# Update Album View
def update_album(request, id):
    myalbum = get_object_or_404(Album, id=id)
    

    if request.method == 'POST':
        # artist name from the POST request
        artist_name = request.POST['artist']
         # Retrieve the artist instance based on the artist name
        artist_instance = get_object_or_404(Artist, Name= artist_name)
        
        myalbum.title = request.POST['title']
        myalbum.artist = artist_instance
        myalbum.release_date = request.POST['release_date']
        myalbum.save()
        return HttpResponseRedirect(reverse('album'))  # Redirect to the album index

    context = {
        'myalbum': myalbum,
    }
    return render(request, 'mysport/update_album.html', context)
 #view album   
def album(request):
    albums = Album.objects.all().values()
    artist_album = Album.objects.all().values('artist')
    albums_count = Album.objects.all().count()
    context = {
        'albums': albums,
        'albums_count': albums_count,
        'artist_album': artist_album,
    }
    
    return render(request, 'mysport/album.html', context)
#signup page
def sign(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')  

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use")
            return render(request, 'mysport/signup.html')

        # Create a new user 
        user = User.objects.create_user(username=email, email=email, password=password)


        # Authenticate and log in the user after successful registration
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('log')  # Redirect to homepage after login
        else:
            messages.error(request, "Unable to log in after signup.")
            return render(request, 'mysport/signup.html')

    return render(request, 'mysport/signup.html')

#login page
def log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "invalid username/password")
            return render (request, 'mysport/login.html')
    else:
        return render(request, 'mysport/login.html')
    
 #view songs   
def music(request):
    music_list = Song.objects.all().values()
    artist_songs = Song.objects.all().count()
    
    context = {
        'music_list': music_list,
        'artist_songs': artist_songs,
    }
    
    return render(request, 'mysport/song.html', context)
#add song
def create_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('music')  
    else:
        form = SongForm()
    return render(request, 'mysport/create_song.html', {'form': form})
#add album
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album')
    else:
        form =AlbumForm()
    return render(request, 'mysport/create_album.html', {'form': form})

# api integration

import urllib.request
import json
from django.shortcuts import render

# My Spotify API key
SPOTIFY_API_KEY = '39ad41994d4048e9b6263342d2480423'

def sport(request):
    data = {}

    if request.method == 'POST':
        # Get the search term from the form
        search_query = request.POST['search_query']
        
        # Encode the search query to make it URL-safe 
        encoded_search_query = urllib.parse.quote(search_query)

        # Spotify API endpoint for searching tracks, albums, or artists
        spotify_url = f'https://api.spotify.com/v1/search?q={encoded_search_query}&type=track&limit=10'

        # Request headers with authorization
        headers = {
            'Authorization': f'Bearer {SPOTIFY_API_KEY}'
        }

        # Creating the request object
        req = urllib.request.Request(spotify_url, headers=headers)

        try:
            # Make the API request and read the response
            with urllib.request.urlopen(req) as response:
                source = response.read()

            # Parsing the JSON response
            list_of_data = json.loads(source)

            # Extract data (e.g., the first track from the search results)
            if list_of_data['tracks']['items']:
                first_result = list_of_data['tracks']['items'][0]
                data = {
                    'track_name': first_result['name'],
                    'artist_name': first_result['artists'][0]['name'],
                    'album_name': first_result['album']['name'],
                    'track_url': first_result['external_urls']['spotify'],
                    'track_image': first_result['album']['images'][0]['url'],
                }
            else:
                data = {'error': 'No results found.'}

        except urllib.error.URLError as e:
            # Handle API request error
            data = {'error': f'Failed to connect to Spotify API: {e}'}

    return render(request, "mysport/index.html", data)
