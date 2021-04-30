from django import forms
from .models import song, album, vocalist, hashtag, language, mood
import django_filters


class addSong(forms.ModelForm):
    class Meta:
        model = song
        exclude = ['isDeleted']


class updateSong(forms.ModelForm):
    class Meta:
        model = song
        fields = ['title']


class updateAlbum(forms.ModelForm):
    class Meta:
        model = song
        fields = ['album_name']


class addAlbum(forms.ModelForm):
    class Meta:
        model = album
        fields = ['album_name']


class updateVocalist(forms.ModelForm):
    class Meta:
        model = song
        fields = ['vocalist_name']


class addVocalist(forms.ModelForm):
    class Meta:
        model = vocalist
        fields = ['vocalist_name']


class updateHashtag(forms.ModelForm):
    class Meta:
        model = song
        fields = ['hashtags']


class addHashtag(forms.ModelForm):
    class Meta:
        model = hashtag
        fields = ['hashtags']


class updateLanguage(forms.ModelForm):
    class Meta:
        model = song
        fields = ['languages']


class addLanguage(forms.ModelForm):
    class Meta:
        model = language
        fields = ['languages']


class updateMood(forms.ModelForm):
    class Meta:
        model = song
        fields = ['moods']


class addMood(forms.ModelForm):
    class Meta:
        model = mood
        fields = ['moods']
