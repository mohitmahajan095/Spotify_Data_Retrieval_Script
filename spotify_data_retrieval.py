"""" MIT License

Copyright (c) 2023 Mohit Mahajan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """"

# Spotify Data Retrieval Script (prints the user's saved tracks, playlists & recently played tracks)
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Get the authentication credentials from user
client_id = input("Enter your Client ID >> ")
client_secret = input("Enter your Client Secret >> ")
redirect_uri = input("Enter your Redirect URI >> ")

# Set up the authentication credentials
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = client_id,
                                               client_secret = client_secret, 
                                               redirect_uri = redirect_uri,
                                               scope = "user-library-read user-read-recently-played"))

# Get the user's saved tracks
saved_tracks = []
results = sp.current_user_saved_tracks()
saved_tracks.extend(results['items'])
while results['next']:
    results = sp.next(results)
    saved_tracks.extend(results['items'])
    
# Get the user's playlists
playlists = []
results = sp.current_user_playlists()
playlists.extend(results['items'])
while results['next']:
    results = sp.next(results)
    playlists.extend(results['items'])
    
# Get the user's recently played tracks
recently_played = []
results = sp.current_user_recently_played()
recently_played.extend(results['items'])
while results['next']:
    results = sp.next(results)
    recently_played.extend(results['items'])

# Print the results for user's saved tracks, playlists & recently played tracks.
print("User's saved tracks: \n")
for track in saved_tracks:
    print(f"{track['track']['name']} by {track['track']['artists'][0]['name']}")

print("\nUser's playlists: \n")
for playlist in playlists:
    print(playlist['name'])

print("\nUser's recently played tracks: \n")
for track in recently_played:
    print(f"{track['track']['name']} by {track['track']['artists'][0]['name']}")

#-by @mohitmahajan095 (github)
