from django.shortcuts import render
from .models import General

# Create your views here.
def home(request):
    general = General.objects.first()
    
    return render(request, 'blog/home.html', {
        general: 'general'
    })