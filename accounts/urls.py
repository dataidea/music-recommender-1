from django.urls import path, include
from .views import signin, signup, signout

urlpatterns = [
    path('signin/', view=signin),
    path('signup/', view=signup),
    path('signout/', view=signout),
]