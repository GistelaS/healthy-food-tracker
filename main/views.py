from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import FoodForm
from main.models import Food

# Create your views here.
def show_main(request):
    foods = Food.objects.all()

    context = {
        'name': 'Gistela Namasya sinurat',
        'class': 'PBP A',
        'foods': foods
    }

    return render(request, "main.html", context)
def create_food(request):
    form = FoodForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_food.html", context)
def show_xml(request):
    data = Food.objects.all()    