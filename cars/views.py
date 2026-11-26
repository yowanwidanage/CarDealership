from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

def home(request):
    cars = Car.objects.filter(is_available=True)
    return render(request, 'home.html', {'cars': cars})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()

    return render(request, 'add_car.html', {'form': form})
