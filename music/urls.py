from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path(route='', view=include('index.urls')),
    path(route='recommendations/', view=include('recommender.urls')),
    path('admin/', admin.site.urls)
]
