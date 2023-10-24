from django.shortcuts import render
from .models import aboutus, sliders, footers, logos

# Create your views here.

def index(request):
    about = aboutus.objects.first()
    slider = sliders.objects.all()
    footer = footers.objects.first()
    logo = logos.objects.first()
    context = {
        'about' : about,
        'slider' : slider,
        'footer' : footer,
        'logo' : logo,
    }

    return render(request, 'index.html', context)