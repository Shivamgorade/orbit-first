# myapp/views.py
from django.shortcuts import render
from orbitapp.models import Card

def home(request):
    card_data = Card.objects.all()
    return render(request, 'orbitapp/index.html', {'card_data': card_data})
