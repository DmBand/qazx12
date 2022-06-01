from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Data


def index(request):
    return render(request, 'app/index.html', context={'title': 'Главная страница'})


def add_data(request):
    if request.method == 'POST':
        if 'reset' in request.POST:
            return render(request, 'app/add_data.html')
        else:
            cleaned_data = request.POST.copy()
            del cleaned_data['csrfmiddlewaretoken']
            Data.objects.create(data=cleaned_data)
            return redirect('app:see_data')
    return render(request, 'app/add_data.html', context={'title': 'Добавить данные'})


def see_data(request):
    data = Data.objects.all().values('data', 'date_added')
    cleaned_data = {}
    for i in data:
        cleaned_data[i['date_added'].strftime("%d.%m.%Y %H:%M:%S")] = i['data']
    return JsonResponse(cleaned_data)
