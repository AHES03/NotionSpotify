from dotenv import load_dotenv
import os
from flask import Flask, render_template
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
load_dotenv()

clientID=os.getenv("API_KEY")
clientSecret=os.getenv("API_SECRET")




sp = Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
                                       client_secret=clientSecret,
                                       redirect_uri='http://localhost:7777/callback',
                                       scope='user-read-playback-state user-modify-playback-state user-read-currently-playing'))

@app.route('/')
def index():
    track_info = sp.current_playback()
    if not track_info:
        album_cover = ''
        song_title = 'No track currently playing'
        artist = ''
    else:
        album_cover = track_info['item']['album']['images'][0]['url']
        song_title = track_info['item']['name']
        artist = track_info['item']['artists'][0]['name']

    return render_template('index.html', album_cover=album_cover, song_title=song_title, artist=artist)

if __name__ == '__main__':
    app.run(debug=True)
