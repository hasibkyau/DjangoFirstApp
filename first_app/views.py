from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album, Person
from first_app import forms
from django.db.models import Avg, Max, Min
# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    album_list = Album.objects.order_by('name')

    diction = {'title':"Home Page", 'musician_list':musician_list, 'album_list':album_list}
    return render(request, 'first_app/index.html', context=diction)

def album_list(request, artist_id):
    # album_list = Album.objects.order_by('name')
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_id).order_by('name','release_date')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))

    diction = {'title':"List of Albums", 'album_list':album_list, 'artist_rating':artist_rating, 'artist_info':artist_info}
    return render(request, 'first_app/album_list.html', context=diction)

def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title':"Add Musician", 'musician_form':form}
    return render(request, 'first_app/musician_form.html', context=diction)


def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title':"Add Album", 'album_form':form}
    return render(request, 'first_app/album_form.html', context=diction)

def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)

        if form.is_valid():
            form.save()
            return album_list(request, artist_id)

    diction = {'edit_form':form, 'artist_id': artist_id}
    return render(request, 'first_app/edit_artist.html', context=diction)
