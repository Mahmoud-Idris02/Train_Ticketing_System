from django.shortcuts import render
# from django.http import HttpResponse
from .models import Trip
from .models import Passenger

# Create your views here.

def home(request):
    if request.method == 'POST':
        from_city = request.POST.get('from')
        to_city = request.POST.get('to')
        trips = Trip.objects.filter(source=from_city, destination=to_city)
        return render(request, 'home/home.html', {'trips': trips})
    else:
        return render(request, 'home/home.html')
    

def book_trip(request):
    message = ''
    if request.method == 'POST':
        # Get the form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNum = request.POST.get('phoneNum')
        tripId = request.POST.get('tripId')
        trainNum = request.POST.get('train-number')
        print("got the values succesfully ")

        # Create a new Passenger object and save it to the database
        passenger = Passenger(name=name, email=email, phoneNum=phoneNum, tripId=tripId, trainNum=trainNum)
        passenger.save()
        print("saved succesfully ")

        # Set the message to display to the user
        message = 'Booking successful!'

    # Render the form template with the message
    return render(request, 'home/home.html', {'message': message})