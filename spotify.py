import os 
import spotipy
import random 
from spotipy.oauth2 import SpotifyClientCredentials

"""os.environ['SPOTIPY_CLIENT_ID'] = 'eed27fb8641a48649bb5c9f9d35106e6'

os.environ['SPOTIPY_CLIENT_SECRET'] = 'aaefc17626a04095b05fff97e2b9d6a4'

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])"""

"""# Set up Spotipy client credentials
client_credentials_manager = SpotifyClientCredentials(client_id='eed27fb8641a48649bb5c9f9d35106e6', client_secret='aaefc17626a04095b05fff97e2b9d6a4')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Choose a random genre
genres = ['pop', 'rock', 'hip-hop', 'jazz', 'classical']
genre = random.choice(genres)

# Search for a playlist in the chosen genre
results = sp.search(q=genre, type='playlist')
playlists = results['playlists']['items']

# Choose a random playlist
playlist = random.choice(playlists)

# Get the tracks in the chosen playlist
tracks = []
results = sp.playlist(playlist['id'])
tracks.extend(results['tracks']['items'])

# Keep getting more tracks if there are more available
while results['tracks']['next']:
    results = sp.next(results['tracks'])
    tracks.extend(results['items'])

# Choose a random track from the playlist
track = random.choice(tracks)

# Get the track details
track_details = sp.track(track['track']['id'])
artist = track_details['artists'][0]['name']
track_name = track_details['name']
album_name = track_details['album']['name']
preview_url = track_details['preview_url']

# Print the chosen track details
print(f"Recommended track: {track_name} by {artist} from the album {album_name}")
if preview_url:
    print(f"Preview available at {preview_url}")
else:
    print("No preview available.")"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'eed27fb8641a48649bb5c9f9d35106e6'
client_secret = 'aaefc17626a04095b05fff97e2b9d6a4'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

query = input("Enter a search query: ")

def search(query):
    results = sp.search(q=query, type='track', limit=50)
    items = results['tracks']['items']
    hindi_items = []
    for item in items:
        if 'hi' in item['album']['available_markets']:
            hindi_items.append(item)
    return hindi_items
"""results = sp.search(query, type='track', limit=10)

if 'tracks' in results and 'items' in results['tracks']:
    tracks = results['tracks']['items']
    for track in tracks:
        print(track['name'], '-', track['artists'][0]['name'])
else:
    print("No tracks found for query:", query)"""

