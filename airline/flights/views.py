from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id) # pk stands for primary key which is the id of the flight in this case
    return render(request, "flights/flight.html", {
        "flight" : flight # passing the second flight variable to flight.html as input
    })