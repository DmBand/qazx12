from django.urls import path

from .views import new_data

app_name = 'app'

urlpatterns = [
    path('', new_data, name='new_data')
]
