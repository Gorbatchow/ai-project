import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="SPOTIPY_CLIENT_ID",
                                               client_secret="SPOTIPY_CLIENT_SECRET",
                                               redirect_uri="SPOTIPY_REDIRECT_URI",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks(limit=50)
all_saved_tracks = results['items']

for idx, item in enumerate(all_saved_tracks):
    track = item['track']
    print(idx + 1, track['artists'][0]['name'], " – ", track['name'])