from django.urls import path
from . import views
urlpatterns = [
    path('', views.sign, name='sign'),
    path('log/', views.log, name="log"),
    path('home/', views.home, name='home'),
    path('artist/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addartist_record, name='addrecord'),
    path('delete/<str:model_type>/<int:id>/', views.delete_object, name='delete_object'),
    path('update/<int:id>', views.update_a, name='update'),
    path('artist/update/<int:id>/', views.update_artist, name='update_artist'),
    path('song/update/<int:id>/', views.update_song, name='update_song'),
    path('album/update/<int:id>/', views.update_album, name='update_album'),
    path('add/view', views.view, name='view'),
    path('album/', views.album, name='album'),
    path('music/', views.music, name='music'),
    path('create-song/', views.create_song, name='create_song'),
    path('create_album/', views.create_album, name='create_album'),
    path('sport/', views.sport, name='sport')
    
    
    
    
]
