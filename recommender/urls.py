from django.urls import path
from . views import recommendations, localMusic

urlpatterns = [
    path('', view=recommendations),
    path(route='local/', view=localMusic)
]