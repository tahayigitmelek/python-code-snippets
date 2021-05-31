import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def show_tracks(results):
    for item in results['items']:
        track = item['track']
        data.write(track['artists'][0]['name']+"-"+track['name']+"\n")

client_credentials_manager=SpotifyClientCredentials(client_id="", client_secret="") #you will fill here according to your client information
    
sp = spotipy.Spotify(auth_manager=client_credentials_manager)

playlists = sp.user_playlists('') #you will fill here to your spotify id

data = open("sptfdata.txt","w",encoding = "utf-8")

for playlist in playlists['items']:
    data.write("\nplaylist name:"+playlist['name']+"\n\n")
    results = sp.playlist(playlist['id'], fields="tracks,next")
    tracks = results['tracks']
    show_tracks(tracks)

    while tracks['next']:
        tracks = sp.next(tracks)
        show_tracks(tracks)

data.close()