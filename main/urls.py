from django.urls import path
from main.views import show_main, create_food, show_xml, show_json, show_xml_by_id, show_json_by_id, create_flutter
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_food
from main.views import delete_food, add_food_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-food', create_food, name='create_food'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-food/<int:id>', edit_food, name='edit_food'),
    path('delete/<int:id>', delete_food, name='delete_food'), # sesuaikan dengan nama fungsi yang dibuat
    path('create-food-ajax/', add_food_ajax, name='add_food_ajax'),
    path("create-flutter/", create_flutter, name="create_flutter"),
]
