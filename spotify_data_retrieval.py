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

#-by @mohitmahajan5824 (github)
