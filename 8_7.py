def make_album(artist, album_name, songs_number=None):
    album = {
        'artist': artist.title(),
        'album_name' : album_name.title()
    }
    if songs_number:
        album['songs_number'] = songs_number
    return album

print(make_album('pink floid', 'the wall'))
print(make_album('pink floid', 'the wall', 26))
    
