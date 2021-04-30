import django_filters
from django import forms
from django.db.models import Q
from .models import song


class songFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='my_custom_filter', label='', widget=forms.TextInput(attrs={'placeholder': 'Search by Audio Title', 'id': 'titleSearch'}))

    class Meta:
        model = song
        fields = ['q', 'album_name', 'vocalist_name']
        widgets = {
            'q': forms.TextInput(attrs={'id': 'search'})
        }

    def my_custom_filter(self, queryset, name, value):
        return song.objects.filter(
            Q(title__icontains=value)
        )
