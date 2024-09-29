from django.db import models
from django.urls import reverse
from django.db.models.functions import Lower
import uuid
# from django import forms
from django.contrib.auth.hashers import make_password


# Create your models here.
# class Loginform(forms.Form):
#     Email = forms.CharField(label='Email', max_length=50)
#     password = forms.CharField(max_length=50)
    
#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
        
#     def __init__(self):
#         return f"{self.Email}"
music_type = (
    ('pop', 'Pop'),
    ('rock', 'Rock'),
    ('jazz', 'Jazz'),
    ('classical', 'Classical'),
    ('hip_hop', 'Hip Hop'),
    ('electronic', 'Electronic'),
)

class Artist(models.Model):
    Name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.Name}"
    
    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"id": self.id})
    

class Album(models.Model):
    title = models.CharField(max_length=50, help_text="Enter music Album")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title}, {self.artist}"
    
class Song(models.Model):
    type = models.CharField(max_length=100, choices=music_type, default=None)
    title = models.CharField(max_length=50, help_text="Enter music title")
    album = models.ManyToManyField(Album)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=1)
    duration = models.DurationField()
    avalability = models.BooleanField(default=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.type}, {self.title}, {self.album}, {self.artist}, {self.duration}"
    
class song_instance(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4)
        song = models.ForeignKey(Song, on_delete=models.CASCADE)
        album = models.ForeignKey(Album, on_delete=models.CASCADE)
        
        song_status = (
            ('a', 'Available'),
            ('p', 'Paid For'),
            ('f', 'free'),
        )
        
        status = models.CharField(max_length=1, choices=song_status, default='a', help_text='song availability')
        
        def __init__(self):
            return f"{self.song}" if self.song else "No song assigned"
    
class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False, default='defaultpassword')

    def __str__(self):
        return f"{self.name},{self.email}, {self.phone_number}"
    
   