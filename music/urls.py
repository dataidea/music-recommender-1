from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home),
    path(route='recommendations/', view=views.recommendations),
    path('admin/', admin.site.urls),
]
