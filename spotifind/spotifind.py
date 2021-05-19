import os
import spotipy
import pprint
import sys
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

if __name__ == "__main__":
    track_name = sys.argv[0]
    load_dotenv()
    scope = 'playlist-read-private'
    client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlists = client.current_user_playlists()

    for i, playlist in enumerate(playlists['items']):
        tracks = client.playlist_items(playlist['id'])
        for i, track in enumerate(tracks['items']):
            pprint.pprint(track['track']['name'])


