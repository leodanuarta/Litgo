from django.shortcuts import render
from .models import aboutus, sliders, footers

# Create your views here.

def index(request):
    about = aboutus.objects.first()
    slider = sliders.objects.all()
    footer = footers.objects.first()
    context = {
        'about' : about,
        'slider' : slider,
        'footer' : footer
    }

    return render(request, 'index.html', context)