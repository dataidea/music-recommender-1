from django.shortcuts import render

# Create your views here.
def recommendations(request):
    recommendations = {
        'songs': ['Beat it', 'Thriller', 'Bad'],
        'artist': 'Micheal Jackson',
        'genre': 'Pop'
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