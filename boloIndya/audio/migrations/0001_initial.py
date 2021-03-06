# Generated by Django 3.1.6 on 2021-03-31 05:10

import audio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='album',
            fields=[
                ('album_id', models.AutoField(primary_key=True, serialize=False)),
                ('album_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='hashtag',
            fields=[
                ('hashtag_id', models.AutoField(primary_key=True, serialize=False)),
                ('hashtags', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('languages', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='mood',
            fields=[
                ('mood_id', models.AutoField(primary_key=True, serialize=False)),
                ('moods', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='vocalist',
            fields=[
                ('vocalist_id', models.AutoField(primary_key=True, serialize=False)),
                ('vocalist_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('audio_file', models.FileField(blank=True, upload_to='media/songs', validators=[audio.models.validate_file_extension])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('album_name', models.ManyToManyField(blank=True, to='audio.album')),
                ('hashtags', models.ManyToManyField(blank=True, to='audio.hashtag')),
                ('languages', models.ManyToManyField(blank=True, to='audio.language')),
                ('moods', models.ManyToManyField(blank=True, to='audio.mood')),
                ('vocalist_name', models.ManyToManyField(blank=True, to='audio.vocalist')),
            ],
        ),
    ]
