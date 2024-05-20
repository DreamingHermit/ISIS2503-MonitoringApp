from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PlaceForm
from .logic.places_logic import get_places, create_place

def place_list(request):
    places = get_places()
    context = {
        'place_list': places
    }
    return render(request, 'Variable/variables.html', context)

def place_create(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            create_place(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created place')
            return HttpResponseRedirect(reverse('placeCreate'))
        else:
            print(form.errors)
    else:
        form = PlaceForm()

    context = {
        'form': form,
    }
    return render(request, 'Place/placeCreate.html', context)