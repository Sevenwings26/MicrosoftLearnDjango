from django.shortcuts import render, get_list_or_404
from .models import Dog, Shelter
# Create your views here.

def shelter_list(request):
    shelters = Shelter.objects.all()
    context = { 'shelters': shelters }
    return render(request, 'shelter_list.html', context)

def shelter_details(request, id):
    shelter = get_list_or_404(Shelter, pk=id)
    context = { 'shelter': shelter }
    return render(request, 'shelter_details.html', context)

