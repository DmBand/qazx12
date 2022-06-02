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
            # Т.к. при стандартных cleaned_data данные сохраняются не очень красиво,
            # то отредактировал их самостоятельно.
            # Было: 01.06.2022 20:04:06: [{name: "data1"},{name: "data2"},{name: "data3"}]
            # Стало: 01.06.2022 20:04:06: {form-0-name: "data1", form-1-name: "data2", form-2-name: "data3"}
            cleaned_data = formset.data.copy()
            del cleaned_data['csrfmiddlewaretoken']
            del cleaned_data['form-TOTAL_FORMS']
            del cleaned_data['form-INITIAL_FORMS']
            del cleaned_data['form-MIN_NUM_FORMS']
            del cleaned_data['form-MAX_NUM_FORMS']
            Data.objects.create(data=cleaned_data)
            return redirect('app:see_data')

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
