from django.shortcuts import render
from joblib import load
from pathlib import Path
from .models import Song
from accounts.models import Profile

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.
def getSongs(genre):
    songs = Song.objects.filter(genre=genre)
    return songs

def recommendations(request):
    profile = Profile.objects.get(user=request.user)
    gender_key_map = {'M':1, 'F':0}

    model = load(f'{BASE_DIR}/recommender/models/model.pkl')
    recommended_genre = model.predict([[profile.age, gender_key_map[profile.gender]]])
    recommendations = {
        'genre': recommended_genre[0],
        'songs': getSongs(genre=recommended_genre[0]),
        'others': Song.objects.all()
    }
    return render(
        request=request,
        template_name='recommender/recommendations.html',
        context=recommendations
    )

def localMusic(request):
    local = {
        'songs': ['Mbada', 'Nakazi', 'Futula'],
        'artist': 'Bobi Wine',
        'genre': 'Ragga'
    }
    return render(
        request=request,
        template_name='recommender/local.html',
        context=local
    )