from django.db import models
from django.conf import settings
import os.path


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.mpeg', '.wav']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.album_name


class hashtag(models.Model):
    hashtag_id = models.AutoField(primary_key=True)
    hashtags = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.hashtags


class vocalist(models.Model):
    vocalist_id = models.AutoField(primary_key=True)
    vocalist_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.vocalist_name


class language(models.Model):
    language_id = models.AutoField(primary_key=True)
    languages = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.languages


class mood(models.Model):
    mood_id = models.AutoField(primary_key=True)
    moods = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.moods


class song(models.Model):
    song_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(
        upload_to='thumbnails', null=True, blank=True)
    audio_file = models.FileField(upload_to='songs', blank=True, null=True,
                                  validators=[validate_file_extension])
    isDeleted = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    album_name = models.ManyToManyField(album, blank=True)
    hashtags = models.ManyToManyField(hashtag, blank=True)
    vocalist_name = models.ManyToManyField(vocalist, blank=True)
    languages = models.ManyToManyField(language, blank=True)
    moods = models.ManyToManyField(mood, blank=True)

    def __str__(self):
        return self.title
