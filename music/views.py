from django.shortcuts import redirect, render
from django.conf import settings
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.http import HttpResponse


######


sp_oauth = SpotifyOAuth(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope='user-read-private user-read-email user-top-read playlist-read-private user-read-playback-state user-modify-playback-state'
)

def get_spotify_client():
    token_info = sp_oauth.get_cached_token()  # Checks if there's a cached valid token

    if not token_info:
        return None  # Redirect to authorization flow if no valid token is found

    # Use the token to initialize a Spotify client
    return spotipy.Spotify(auth=token_info['access_token'])

def spotify_auth(request):
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def spotify_callback(request):
    code = request.GET.get('code')
    token_info = sp_oauth.get_access_token(code) # Retrieve and cache the token
    
    # Redirect to any view where you need to use Spotify API after successful login
    return redirect('/')

def get_user_profile(request):
    spotify = get_spotify_client()
    if not spotify:
        return redirect('spotify_auth')  # Redirect to auth if no valid token
    
    try:
        user = spotify.current_user()
        top_artists = spotify.current_user_top_artists(limit=5, time_range='long_term')
        top_tracks = spotify.current_user_top_tracks(limit=5, time_range='long_term')

        context = {
            'user': user,
            'top_artists': top_artists,
            'top_tracks': top_tracks,
        }

        return render(request, 'profile.html', context=context)
    except spotipy.exceptions.SpotifyException as e:
        return HttpResponse(f"Spotify error: {e}", status=400)
    

def get_playlist(request):
    spotify = get_spotify_client()
    if not spotify:
        return redirect('spotify_auth')  # Redirect to auth if no valid token

    try:
        playlist_id = "5VO4QF2GLvC0D58p740DnB"  # Example playlist ID
        playlist = spotify.playlist_tracks(playlist_id, additional_types=('track'))
        
        return render(request, 'playlist.html', {'playlist': playlist})
    except spotipy.exceptions.SpotifyException as e:
        return HttpResponse(f"Spotify error: {e}", status=400)

