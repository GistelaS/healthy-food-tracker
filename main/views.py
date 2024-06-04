import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import FoodForm
from main.models import Food
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    foods = Food.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'foods': foods,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
def create_food(request):
 form = FoodForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     food = form.save(commit=False)
     food.user = request.user
     food.save()
     return redirect('main:show_main')

 context = {'form': form}
 return render(request, "create_food.html", context)
 ...
def show_xml(request):
    data = Food.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Food.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Food.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Food.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
def edit_food(request, id):
    # Get food berdasarkan ID
    food = Food.objects.get(pk = id)

    # Set food sebagai instance dari form
    form = FoodForm(request.POST or None, instance=food)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_food.html", context)
def delete_food(request, id):
    # Get data berdasarkan ID
    food = Food.objects.get(pk = id)
    # Hapus data
    food.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def add_food_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        calories = request.POST.get("calories")
        description = request.POST.get("description")
        user = request.user

        new_food = Food(name=name, calories=calories, description=description, user=user)
        new_food.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_food = Food.objects.create(
            user = request.user,
            name = data["food"],
            calories = int(data["calories"]),
            description = data["description"]
        )

        new_food.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)