from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from audio.models import song, album
from audio.forms import addSong, updateSong, addAlbum, addVocalist, addHashtag, addLanguage, addMood, updateVocalist, updateMood, updateHashtag, updateLanguage, updateAlbum
from audio.filters import songFilter
# Create your views here.


def main(request):
    my_dict = {
        'its_me': "Im coming from the other side of views.py"
    }
    return render(request, "audio/index.html", context=my_dict)


def uploadSong(request):
    form = addSong(request.POST or None, request.FILES or None)
    if (request.method == "POST"):
        if form.is_valid():
            form.save(commit=True)
            return redirect(songs)
        else:
            print("ERROR FROM INVALID FORM")
    return render(request, 'audio/uploadSong.html', {'form': form})


def deleteSong(request, id):
    songdel = song.objects.get(pk=id)
    mydict = {'song': songdel}
    if (request.method == "POST"):
        songdel.isDeleted = True
        songdel.save()
        return redirect(songs)
    else:
        print("ERROR FROM INVALID FORM")
    return render(request, 'audio/delete.html', context=mydict)


def UpdateSong(request, id):
    titles = song.objects.get(pk=id)
    form = updateSong(request.POST or None, instance=titles)
    if (request.method == "POST"):
        if form.is_valid():
            form.save(commit=True)
            return redirect(songs)
        else:
            print("ERROR FROM INVALID FORM")
    return render(request, 'audio/updateTitle.html', {'form': form})


def UpdateAlbum(request, id):
    albums = song.objects.get(pk=id)
    album = song.objects.get(pk=id).album_name
    albumForm = updateAlbum(request.POST or None, instance=albums)
    addAlbumForm = addAlbum(request.POST or None)
    data_dict = {'album': album, 'form': albumForm, 'addForm': addAlbumForm}
    if request.method == 'POST' and 'add' in request.POST:
        if addAlbumForm.is_valid():
            addAlbumForm.save(commit=True)
            return render(request, 'audio/update_album.html', context=data_dict)
    if request.method == 'POST' and 'update' in request.POST:
        if albumForm.is_valid():
            albumForm.save(commit=True)
            return redirect(songs)
        else:
            print("ERROR FROM INVALID FORM")
    return render(request, 'audio/update_album.html', context=data_dict)


def UpdateVocalist(request, id):
    vocalists = song.objects.get(pk=id)
    vocalist = song.objects.get(pk=id).vocalist_name
    vocalistForm = updateVocalist(request.POST or None, instance=vocalists)
    addVocalistForm = addVocalist(request.POST or None)
    data_dict = {'vocalist': vocalist,
                 'form': vocalistForm, 'addForm': addVocalistForm}
    if request.method == 'POST' and 'add' in request.POST:
        if addVocalistForm.is_valid():
            addVocalistForm.save(commit=True)
            return render(request, 'audio/update_vocalist.html', context=data_dict)
    if request.method == 'POST' and 'update' in request.POST:
        if vocalistForm.is_valid():
            vocalistForm.save(commit=True)
            return redirect(songs)
        else:
            print("ERROR FROM INVALID FORM")
    return render(request, 'audio/update_vocalist.html', context=data_dict)


def UpdateHashtag(request, id):
    hashtags = song.objects.get(pk=id)
    hashtag = song.objects.get(pk=id).hashtags
    hashtagForm = updateHashtag(request.POST or None, instance=hashtags)
    addHashtagForm = addHashtag(request.POST or None)
    data_dict = {'hashtag': hashtag,
                 'form': hashtagForm, 'addForm': addHashtagForm}
    if request.method == 'POST' and 'add' in request.POST:
        if addHashtagForm.is_valid():
            addHashtagForm.save(commit=True)
            return render(request, 'audio/update_hashtag.html', context=data_dict)
    if request.method == 'POST' and 'update' in request.POST:
        if hashtagForm.is_valid():
            hashtagForm.save(commit=True)
            return redirect(songs)
        else:
            print("ERROR FROM INVALID FORM")
    return render(request, 'audio/update_hashtag.html', context=data_dict)


def UpdateLanguage(request, id):
    languages = song.objects.get(pk=id)
    language = song.objects.get(pk=id).languages
    languageForm = updateLanguage(request.POST or None, instance=languages)
    addLanguageForm = addLanguage(request.POST or None)
    data_dict = {'language': language,
                 'form': languageForm, 'addForm': addLanguageForm}
    if request.method == 'POST' and 'add' in request.POST:
        if addLanguageForm.is_valid():
            addLanguageForm.save(commit=True)
            return render(request, 'audio/update_language.html', context=data_dict)
    if request.method == 'POST' and 'update' in request.POST:
        if languageForm.is_valid():
            languageForm.save(commit=True)
            return redirect(songs)
        else:
            print("ERROR FROM INVALID FORM")
    return render(request, 'audio/update_language.html', context=data_dict)


def UpdateMood(request, id):
    moods = song.objects.get(pk=id)
    mood = song.objects.get(pk=id).moods
    moodForm = updateMood(request.POST or None, instance=moods)
    addMoodForm = addMood(request.POST or None)
    data_dict = {'mood': mood,
                 'form': moodForm, 'addForm': addMoodForm}
    if request.method == 'POST' and 'add' in request.POST:
        if addMoodForm.is_valid():
            addMoodForm.save(commit=True)
            return render(request, 'audio/update_mood.html', context=data_dict)
    if request.method == 'POST' and 'update' in request.POST:
        if moodForm.is_valid():
            moodForm.save(commit=True)
            return redirect(songs)
        else:
            print("ERROR FROM INVALID FORM")
    return render(request, 'audio/update_mood.html', context=data_dict)


def songs(request):
    model = song
    songs = song.objects.filter(isDeleted=False).order_by('uploaded_at')
    myFilter = songFilter(request.GET, queryset=songs)
    songs = myFilter.qs
    song_dict = {
        'songs': songs, 'form': myFilter
    }
    return render(request, 'audio/songs.html', context=song_dict)


def songpost(request, id):
    s = song.objects.filter(pk=id).first()
    data = dict()
    songs = song.objects.filter(isDeleted=False).order_by('uploaded_at')
    context = {'s': s, 'songs': songs}
    data['html_song_list'] = render_to_string(
        'audio/dupe.html', context, request=request)
    data['html_form'] = render_to_string(
        'audio/songpost.html', context, request=request)
    return JsonResponse(data)


def filterSong(request):
    model = song
    songs = song.objects.order_by('title')
    myFilter = songFilter(request.GET, queryset=songs)
    songs = myFilter.qs
    data_dict = {'songs': songs, 'form': myFilter}
    return render(request, 'audio/songSearch.html', context=data_dict)
