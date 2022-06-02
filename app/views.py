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
            print(dir(formset))
            print(formset.data)
            print(formset.cleaned_data)
            data = formset.data.copy()
            del data['csrfmiddlewaretoken']
            del data['form-TOTAL_FORMS']
            del data['form-INITIAL_FORMS']
            del data['form-MIN_NUM_FORMS']
            del data['form-MAX_NUM_FORMS']
            print('data:', data)
            # Data.objects.create(data=formset.cleaned_data)
            # return redirect('app:see_data')

    context = {
        'title': 'Добавить данные',
        'formset': formset
    }

    return render(request, 'app/add_data.html', context)


def see_data(request):
    """ Страница просмотра данных """

    data = Data.objects.all().values('data', 'date_added')
    print(data)
    cleaned_data = {}
    for i in data:
        cleaned_data[i['date_added'].strftime("%d.%m.%Y %H:%M:%S")] = i['data']
    return JsonResponse(cleaned_data)
