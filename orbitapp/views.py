from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Card
from .models import Quote
import random 
from .forms import SeniorRegistrationForm
from .models import Senior

#home page 
def search_seniors(request):
    expertise_query = request.GET.get('expertise')

    # Filter seniors by expertise
    seniors = Senior.objects.filter(expertise__icontains=expertise_query)

    return render(request, 'orbitapp/find_senior.html', {'seniors': seniors})

def home(request):
    quotes = Quote.objects.all()
    random_quote = None

    if quotes:
        random_quote = random.choice(quotes)

    print("Quotes:", quotes)
    print("Random Quote:", random_quote)

    return render(request, 'orbitapp/home.html', {'random_quote': random_quote})

#page for find job



def find_job(request):
    query = request.GET.get('q')
    card_data = Card.objects.all()

    if query:
        card_data = card_data.filter(
            Q(company_name__icontains=query) | Q(location__icontains=query) | Q(designation__icontains=query)
        )

    return render(request, 'orbitapp/find_job.html', {'card_data': card_data, 'query': query})

#page for find talent 

def find_talent(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        designation = request.POST['designation']
        apply_link = request.POST['apply_link']
        location = request.POST['location']
        qualification = request.POST['qualification']
        salary= request.POST['salary']
        experience = request.POST['experience']

        # Prepend "http://" if the URL doesn't start with a scheme
        if not apply_link.startswith(('http://', 'https://')):
            apply_link = 'http://' + apply_link

        card = Card(
            company_name=company_name,
            designation=designation,
            apply_link=apply_link,
            location=location,
            qualification=qualification,
            salary=salary,
            experience=experience,
        )
        card.save()

    return render(request, 'orbitapp/find_talent.html')
#page for find senior 

def register_senior(request):
    if request.method == 'POST':
        form = SeniorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_senior')

    else:
        form = SeniorRegistrationForm()

    return render(request, 'orbitapp/uni-connect.html', {'form': form})

def show_senior(request):
    seniors = Senior.objects.all()
    return render(request, 'orbitapp/find_senior.html', {'seniors': seniors})
