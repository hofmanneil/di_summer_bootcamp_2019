import sqlite3

class Album:
    all_albums=[]
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    @classmethod          #factory build list of album names
    def fetch_album(cls, cursor):
        cursor.execute('''
        SELECT ArtistId,Title
        FROM albums    
        ''')
        result = cursor.fetchall()
        all_albums = []
        for record in result:
            all_album = cls(record[0], record[1])
            all_albums.append(all_album)
        return all_albums


class Artist:
    all_artists = []
    def __init__(self, artistId, name):
        self.name = name
        self.id = artistId
    @classmethod
    def fetch_artist(cls, cursor):
        cursor.execute('''SELECT ArtistId,Name
        FROM artists
        ''')
        result = cursor.fetchall()  # for 1 entry row= cursor.fetchone
        all_artist = []
        for record in result:
            all_artist.append(cls(record[0], record[1]))
        return all_artist

class Tracks:
    all_tracks = []
    def __init__(self, name, album):
        self.album=[]
        self.name = name
    @classmethod
    def get_tracks(cls, cursor):
        cursor.execute('''SELECT ArtistId,name ,Title
                FROM tracks,albums
                ''')
        rec = cursor.fetchall()
        all_tracks = []
        for track in rec:
            all_tracks.append(cls(track[1], track[2]))
            return all_tracks

    @classmethod
    def get_artist_track(cls,name):
        cursor.execute('''SELECT tracks.Name,artists.Name
    FROM artists,tracks,albums
    WHERE tracks.AlbumId =albums.AlbumId AND artists.ArtistId = albums.ArtistId
    ''')
        record2 = cursor.fetchall()
        artist_track = []
        for at in record2:
            artist_track.append(cls.at[1], at[2])
        return artist_track





#+++++++++++Main Code ++++++++
db = sqlite3.connect('chinook.db')
cursor = db.cursor()
all_artists = Artist.fetch_artist(cursor)
all_albums = Album.fetch_album(cursor)
all_tracks = Tracks.get_tracks(cursor)
#artist_track = Tracks.get_artist_track(cursor)
#print all artist
for artist in all_artists:
    print(artist.name)

#print albums
for albums in all_albums:
    print(albums.title)
#print tracks
for tracks in all_tracks:
    print(tracks.name)

#track and artist
#for al in artist_track:
#    print(al)







#album_name_search = input('Which album do you want to search for ?')

#for track in tracks:
#    if track.album.title== album_name_search:
#        album_found=track.album
#        break

#print(album_found.tracks)










#ask user for name of album
# 1 Display all albums
# 2 Display all tracks of album
# 3 Display all albums of an artist
# 4 Display all tracks of an artist
