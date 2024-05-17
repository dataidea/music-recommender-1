from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)
            return redirect('/recommendations')
    else:
        form = AuthenticationForm()
        context = {'form': form}
    return render(
        request=request,
        template_name='accounts/signin.html',
        context=context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/signin')
    else:
        form = CustomUserCreationForm()
        context = {'form': form}
    return render(
        request=request, 
        template_name='accounts/signup.html', 
        context=context)

def signout(request):
    pass
