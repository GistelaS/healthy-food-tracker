from django.urls import path
from main.views import show_main, create_food, show_xml

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-food', create_food, name='create_food'),
    path('xml/', show_xml, name='show_xml'),
]
