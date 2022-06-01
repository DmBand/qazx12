from django.shortcuts import render


def new_data(request):

    if request.method == 'POST':
        print(request.POST)
        if 'reset' in request.POST:
            return render(request, 'app/index.html')
    return render(request, 'app/index.html')
