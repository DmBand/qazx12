from django.urls import path

from .views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('add_data', add_data, name='add_data'),
    path('see_data', see_data, name='see_data'),
]
