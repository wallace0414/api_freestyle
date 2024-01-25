"""
A program kezdéskor megkérdezi a felhasználótól, hogy melyik funkciót szeretné használni.
Az 1. funkció a legújabba albummegjelenéseket irja ki a felhasználónak.
A 2. funkció a felhasználó által megadott 1 vagy több előadó alapján ajánl a felhasználónak dalokat.
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth

redirect_uri = "http://127.0.0.1:9090"
client_id = '24faac524bdf4fa38bfa1c0d783be130'
client_secret = '9f1c211c75134215aa684e391331078a'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret))


def get_releases():
    result = sp.new_releases(limit=10)
    index = 1
    for album in result['albums']['items']:
        album_name = album['name']
        artists_name = []
        for i in album['artists']:
            artists_name.append(i['name'])
        print(f'{index}. {album_name} - {", ".join(artists_name)}')
        index += 1


def get_recommendations():
    artists = input('Add meg az elöadők nevét!  ').split(',')
    ids = []
    for artist in artists:
        q = artist
        result = sp.search(q, type='artist')
        ids.append(result['artists']['items'][0]['id'])

    result = sp.recommendations(seed_artists=ids, limit=10)
    index = 1
    for track in result['tracks']:
        artists_name = []
        for i in track['artists']:
            artists_name.append(i['name'])
        track_name = track['name']
        print(f'{index}. {track_name} - {", ".join(artists_name)}')
        index += 1


def main():
    print('1  Új albummegjelenések \n'
          '2  Új számok ajánlása előadó(k) alapján \n')
    choosen_number = int(input('Add meg a választott funkció számát!  '))
    if choosen_number == 1:
        get_releases()
    elif choosen_number == 2:
        get_recommendations()


main()
