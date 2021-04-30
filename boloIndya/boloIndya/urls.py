"""boloIndya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from audio.views import main, songs, songpost, deleteSong, uploadSong, UpdateSong, filterSong, UpdateMood, UpdateLanguage, UpdateAlbum, UpdateVocalist, UpdateHashtag
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', main, name='main'),
    path('upload/', uploadSong, name='uploadSong'),
    path('audio/', include('audio.urls')),
    path('songs/<int:id>', songpost, name='songpost'),
    path('songs/update-album/<int:id>', UpdateAlbum, name="UpdateAlbum"),
    path('songs/update-hashtag/<int:id>', UpdateHashtag, name="UpdateHashtag"),
    path('songs/update-mood/<int:id>', UpdateMood, name="UpdateMood"),
    path('songs/update-title/<int:id>', UpdateSong, name="UpdateSong"),
    path('songs/delete/<int:id>', deleteSong, name="deleteSong"),
    path('songs/update-language/<int:id>',
         UpdateLanguage, name="UpdateLanguage"),
    path('songs/update-vocalist/<int:id>',
         UpdateVocalist, name="UpdateVocalist"),
    path('songs/', songs, name='songs'),
    path('search/', filterSong, name="filterSong"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
