from django.shortcuts import render
from .models import LoveCalculator
import random

def index(request):
    return render(request, 'main/index.html')

def calculate_love(request):
    if request.method == 'POST':
        person1_name = request.POST['person1_name']
        person2_name = request.POST['person2_name']
        love_percentage = random.randint(1, 101)

        love_calculation = LoveCalculator.objects.create(person1_name=person1_name, person2_name=person2_name, love_percentage=love_percentage)

        return render(request, 'main/result.html', {'love_percentage': love_percentage})

    return render(request, 'main/index.html')
