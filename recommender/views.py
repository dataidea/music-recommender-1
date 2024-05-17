from django.shortcuts import render
from joblib import load
from pathlib import Path
from .models import Song

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.
def getSongs(genre):
    songs = Song.objects.filter(genre=genre)
    return songs

def recommendations(request):
    model = load(f'{BASE_DIR}/recommender/models/model.pkl')
    recommended_genre = model.predict([[15, 1]])
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