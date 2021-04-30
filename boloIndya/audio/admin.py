from django.contrib import admin
from audio.models import song, album, language, mood, hashtag, vocalist
# Register your models here.

admin.site.register(song)
admin.site.register(album)
admin.site.register(language)
admin.site.register(mood)
admin.site.register(hashtag)
admin.site.register(vocalist)
