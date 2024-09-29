from django.contrib import admin
from .models import Artist, Album, Song, user, song_instance

# Register your models here.
#admin.site.register(Album)
@admin.register(Album)

class Albumadmin(admin.ModelAdmin):
    list_display = (
        'title', 'artist', 'release_date'
    )
    list_filter = ['release_date']
    fieldsets = (
        (None, {
            "fields": (
                'title', 'artist',
            ),
        }),
        ('Availability', {
            "fields":[
                'release_date'
            ]
        })
    )

#admin.site.register(Artist)
@admin.register(Artist)
class Artistadmin(admin.ModelAdmin):
    list_display = (
        'Name', 'bio'
    )
#admin.site.register(song)
@admin.register(Song)
class songadmin(admin.ModelAdmin):
    list_display =(
        'title', 'duration'
    )
    list_filter = ['album']
    fieldsets = (
        (None, {
            "fields":(
                'type', 'title', 'artist'
            )
        }),
        ('Availabilty',{
            "fields":(
                'album', 'duration', 'release_date'
            )
        })
    )
    
@admin.register(song_instance)
class instance_admin(admin.ModelAdmin):
    list_display =(
       'id', 'song', 'album', 'status' 
    )
    
#admin.site.register(user)
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display =(
        'name', 'email', 'phone_number', 'password'
    )
    list_filter =['name']
