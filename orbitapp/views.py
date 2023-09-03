from django.shortcuts import render
from django.db.models import Q
from .models import Card

def home(request):
    # Add any data or logic you need for this view
    return render(request, 'orbitapp/home.html') 


def find_job(request):
    query = request.GET.get('q')
    card_data = Card.objects.all()

    if query:
        card_data = card_data.filter(
            Q(company_name__icontains=query) | Q(location__icontains=query) | Q(designation__icontains=query)
        )

    return render(request, 'orbitapp/find_job.html', {'card_data': card_data, 'query': query})
