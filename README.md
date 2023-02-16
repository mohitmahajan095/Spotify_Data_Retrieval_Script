![ezgif-3-2bb9aceb35](https://user-images.githubusercontent.com/73893201/219341706-2dc1f1a2-a49e-4d20-bacd-f1643ce32b26.gif)



# Spotify Data Retrieval Script
**Spotify Data Retrieval Script:** A Python script that uses Spotipy to interact with the Spotify Web API and retrieve a user's saved tracks, playlists, and recently played tracks. Outputs to console.

# Installation                     
To use this script, you will need to install the Spotipy library. You can do this using pip:

**pip install spotipy**

# Usage
1. Clone this repository to your local machine.
2. Enter your Spotify client ID, client secret, and redirect URI when prompted.
3. Run the script using the command :
   
   **python spotify_data_retrieval.py**

The script will then retrieve the user's saved tracks, playlists, and recently played tracks, and print them out to the console.

# Steps to obtain developer credentials (Client ID, Client Secret & Redirect URI).

1. Go to https://developer.spotify.com/dashboard/ and log in to your Spotify account (or create a new account if you don't have one).

2. Create a new app by clicking the "Create an App" button and fill in the required information.

3. Once your app is created, you will see the "Client ID" and "Client Secret" on the app dashboard. Copy these values to a secure location, as you will need them later.

4. Add the "Redirect URI" for your app by clicking the "Edit Settings" button and entering the URI under the "Redirect URIs" section. This URI will be used to authenticate your app and obtain an access token for the Spotify API (eg. https://open.spotify.com/? ).

**Note : You can also use environment variables to store your credentials and access them in your code.**

# Instructions for using the Spotify Data Retrieval Script.

After obtaining the Client ID, Client Secret & Redirect URI,

1. Install the Spotipy library by running **pip install spotipy** in your terminal. (in case if you don't have)

2. Download the script from the repository.

3. Open the script in your preferred code editor/terminal.

4. Paste your client_id, client_secret, and redirect_uri values in the input() function at the beginning of the script.

5. Run the script.

6. The script will prompt you to authenticate with Spotify through the browser.

7. Once authenticated, the script will retrieve your saved tracks, playlists, and recently played tracks from your Spotify account and display them in the console.
