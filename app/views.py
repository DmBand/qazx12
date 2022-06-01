from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import DataForm, DataFormset
from .models import Data


def index(request):
    """ Главная страница """

    return render(request, 'app/index.html', context={'title': 'Главная страница'})


def add_data(request, *args, **kwargs):
    """ Страница ввода данных """

    if request.method != 'POST':
        formset = DataFormset()
    else:
        formset = DataFormset(data=request.POST)
        if formset.is_valid():
            Data.objects.create(data=formset.cleaned_data)
            return redirect('app:see_data')

    context = {
        'title': 'Добавить данные',
        'formset': formset
    }

    return render(request, 'app/add_data.html', context)


def see_data(request):
    """ Страница просмотра данных """

    data = Data.objects.all().values('data', 'date_added')
    cleaned_data = {}
    for i in data:
        cleaned_data[i['date_added'].strftime("%d.%m.%Y %H:%M:%S")] = i['data']
    return JsonResponse(cleaned_data)
