from django.shortcuts import render
from django.db.models import Q
from .models import Card
from .models import Quote
import random 

def home(request):
    quotes = Quote.objects.all()
    random_quote = None

    if quotes:
        random_quote = random.choice(quotes)

    print("Quotes:", quotes)
    print("Random Quote:", random_quote)

    return render(request, 'orbitapp/home.html', {'random_quote': random_quote})
def find_job(request):
    query = request.GET.get('q')
    card_data = Card.objects.all()

    if query:
        card_data = card_data.filter(
            Q(company_name__icontains=query) | Q(location__icontains=query) | Q(designation__icontains=query)
        )

    return render(request, 'orbitapp/find_job.html', {'card_data': card_data, 'query': query})
