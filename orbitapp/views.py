from django.shortcuts import render
from django.db.models import Q  # Import the Q object
from .models import Card

def home(request):
    query = request.GET.get('q')
    card_data = Card.objects.all()

    if query:
        card_data = card_data.filter(
            Q(company_name__icontains=query) | Q(location__icontains=query) | Q(designation__icontains=query)
        )

    return render(request, 'orbitapp/index.html', {'card_data': card_data, 'query': query})
