from django.shortcuts import render

def home(request):
    return render(
        request=request, 
        template_name='home.html')

def recommendations(request):
    return render(
        request=request,
        template_name='recommendations.html')