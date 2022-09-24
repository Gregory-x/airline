from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id) # pk stands for primary key which is the id of the flight in this case
    return render(request, "flights/flight.html", {
        "flight" : flight, # passing the second flight variable to flight.html as input
        "passengers" : flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight) # you need to get all the passengers to choose from

    })

def book(request, flight_id):
    if request.method=="POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args = (flight.id,))) # redirects back to the flight route, reverses the name back to the link
