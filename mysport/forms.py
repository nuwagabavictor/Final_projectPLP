from django import forms
from .models import Song, Album

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['type', 'title', 'album', 'artist', 'duration', 'release_date']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'duration': forms.TimeInput(attrs={'type': 'time'}),
        }
        
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_date']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }
